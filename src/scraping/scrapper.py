# My imports
from scraping.browserInstance.makeChromeInstance import makeBrowser
from scraping.utils import URL, WAITING_TIME
from scraping.xlsxWriter import writeXlsxFile

# Selenium imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# Beautiful soup imports
from bs4 import BeautifulSoup

# Math imports
from math import floor

# Time lib imports
from time import sleep


def verifyStudantInformation(registrationNumber: str, password: str) -> bool:
    """Get the info from the studant from registerUserController and verify if the user exists

    RETURNS: True if the user exists and False if not
    """

    # Create a browser instance
    chromeBrowser = makeBrowser("--headless")
    chromeBrowser.get(URL)

    # Wait to find input on screen
    loginInput = WebDriverWait(chromeBrowser, WAITING_TIME).until(
        # Finding an element on the screen
        EC.presence_of_element_located((By.ID, "codigo"))
    )

    passwordInput = WebDriverWait(chromeBrowser, WAITING_TIME).until(
        # Finding an element on the screen
        EC.presence_of_element_located((By.ID, "senha"))
    )

    # Write your login and password then press enter
    loginInput.send_keys(registrationNumber)
    passwordInput.send_keys(password)
    loginInput.send_keys(Keys.ENTER)

    try:
        WebDriverWait(chromeBrowser, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        chromeBrowser.quit()
        return False
    except TimeoutException:
        return True


class Scrapper:
    def __init__(self, username: str, registrationNumber: str, password: str) -> None:
        self.studantUsername = username

        self.subjectNamesList = []
        self.subjectPagesHtml = []
        self.formatedSubjectsData = []

        # Create a browser instance
        self.chromeBrowser = makeBrowser()
        self.chromeBrowser.get(URL)

        self.loginCesuscWebsite(registrationNumber, password)
        self.acessingGradesAndFrequency()
        self.settingIframeToChromeDriver()
        self.getSubjectsNames()
        self.getSubjectPagesHtml()
        self.formatingSubejectData()

    def getFormatedSubjectData(self):
        return self.formatedSubjectsData

    def loginCesuscWebsite(self, registrationNumber: str, password: str):
        """This method is responsible for login in the cesusc website"""

        # Wait to find input on screen
        loginInput = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            # Finding an element on the screen
            EC.presence_of_element_located((By.ID, "codigo"))
        )

        passwordInput = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            # Finding an element on the screen
            EC.presence_of_element_located((By.ID, "senha"))
        )

        # Write your login and password then press enter
        loginInput.send_keys(registrationNumber)
        passwordInput.send_keys(password)
        loginInput.send_keys(Keys.ENTER)

    def acessingGradesAndFrequency(self):
        """This method is responsible for acessing the grades and frequency page"""

        # Get the lateral menu
        gradesAndFrequencyButton = self.chromeBrowser.find_elements(
            By.CLASS_NAME, "btnMenuLateral"
        )

        # Passing through all the buttons in the lateral menu and finding the grades and frequency button
        for gradesAndFrequency in gradesAndFrequencyButton:
            if gradesAndFrequency.text == "Notas e Frequências":
                gradesAndFrequencyButton = gradesAndFrequency

        # Click on the grades and frequency button
        gradesAndFrequencyButton.click()

    def settingIframeToChromeDriver(self):
        """This method is responsible for setting the iframe to the chrome driver"""

        iframeWithHTML = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            # Finding an element on the screen
            EC.presence_of_element_located(
                (
                    By.ID,
                    "iframe_conteudo",
                )
            )
        )

        self.chromeBrowser.switch_to.frame(iframeWithHTML)

    def getSubjectsNames(self) -> None:
        """Set the class internal variable  subjectNamesList"""
        sleep(3)
        # Wait for the table to be fully loaded and select it
        table = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div[6]/table"))
        )

        # Get the table of the subjects using searching by tag name
        subjectsRows = table.find_elements(By.TAG_NAME, "tr")

        # Appeding the subject names to the list skiping the first row because it's the header
        for i in range(1, len(subjectsRows)):
            self.subjectNamesList.append(
                # Removes the name of the teacher from the subject name
                subjectsRows[i].text[: subjectsRows[i].text.find("\n")]
            )

    def getSubjectPagesHtml(self) -> None:
        # Wait for the table to be fully loaded and select it
        table = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@class='slim highlight']")
            )
        )

        # Get the table of the subjects by tag name
        subjectsRows = table.find_elements(By.TAG_NAME, "tr")

        # Passing through all the subjects
        for i in range(1, len(subjectsRows)):
            # We need to get the table again because the page reloads
            if i != 1:
                subjectsRows = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//table[@class='slim highlight']")
                    )
                )

                subjectsRows = subjectsRows.find_elements(By.TAG_NAME, "tr")

            # Click on the subject
            temp = subjectsRows[i].find_element(By.TAG_NAME, "td")
            temp.click()

            # Append the html to the list of htmls
            self.subjectPagesHtml.append(self.chromeBrowser.page_source)

            # Wait for the return button to be loaded and click on it to return to the grades and frequency page
            returnButton = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-voltar"))
            )
            returnButton.click()

    def formatingSubejectData(self):
        # Importing the function that will format the data, this import is here to avoid circular imports
        from scraping.dataMining import formatData

        for index, subjectHtml in enumerate(self.subjectPagesHtml):
            # parse the html to a bs4 object
            soup = BeautifulSoup(subjectHtml, "html.parser")

            # select the main table body
            tableBody = soup.select_one(
                "table.u-responsive-table:nth-child(4) > tbody:nth-child(3)"
            )

            # select all rows
            tableRows = tableBody.find_all("tr")

            # Select the table that has the frequency
            frequencyTable = soup.select(
                "table.u-responsive-table.on-medium.with-label-top.with-border.white.z-depth-1.u-margin-20-0"
            )

            lastTableData = frequencyTable[-1].select('td[data-label="Número da Aula"]')

            # Checks if the frequency is not empty
            if lastTableData != []:
                # Get the total of classes in the subject
                maxClassesInSubject = lastTableData[-1].text.strip()

                # Calculate the max classes that the student can skip
                maxClassSkip = floor((float(maxClassesInSubject) * 75) / 100) - int(
                    maxClassesInSubject
                )
                maxClassSkip *= -1

            # Try to get the frequency in percentage that is on the table in the footer of the page, if it doesn't exist, it means that this class doesn't have frequency
            try:
                frequencyInPercentage = soup.select_one(
                    "table.u-responsive-table:nth-child(6) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(5)"
                ).text
            except AttributeError:
                frequencyInPercentage = "Disciplina sem registros."

            if lastTableData != []:
                # Remove the % from the string and convert it to int
                yourMissedClasses = frequencyInPercentage[
                    : frequencyInPercentage.find("%")
                ].strip()

                # Get the number of classes that you get present in the subject
                yourMissedClasses = floor(
                    (float(maxClassesInSubject) * int(yourMissedClasses)) / 100
                )

                # Calculate the number of misses that you have
                yourMissedClasses -= int(maxClassesInSubject)
                yourMissedClasses *= -1

                # Caluclate how mutch classes you can miss without getting reproved, based on 75% of presence
                howMutchYouCanMiss = maxClassSkip - yourMissedClasses

                # Check if you can miss more classes
                if howMutchYouCanMiss < 0:
                    howMutchYouCanMiss = (
                        f"Você já passou do limite de faltas ({howMutchYouCanMiss})."
                    )
            else:
                maxClassSkip = "Materia ainda não tem registros."
                yourMissedClasses = "Materia ainda não tem registros."
                howMutchYouCanMiss = "Materia ainda não tem registros."

            self.formatedSubjectsData.append(
                formatData(
                    tableRows,
                    self.subjectNamesList[index],
                    maxClassSkip,
                    yourMissedClasses,
                    frequencyInPercentage,
                    howMutchYouCanMiss,
                )
            )

        # uses the formated info to write a xlsx file
        writeXlsxFile(self.formatedSubjectsData, self.studantUsername)


def getStudantGradeAverage(grades: list[str]) -> float | int:
    """This function receives a list of grades from a studant and returns the average of the grades dividing by the length of the list"""

    # Variable where the average will be alocated
    average = 0
    count = 0

    # Passing through all the grades
    for i in range(len(grades)):
        gradeValue = grades[i].find(attrs={"data-label": "Nota"})

        # Check if the grade is defined by the teacher, if not, don't count it
        if gradeValue.text.strip() == "-":
            average += 0
        else:
            count += 1
            # Replace the comma with a dot and convert it to float
            average += float(gradeValue.text.strip().replace(",", "."))

    # Checks if the count is 0, if it is, it means that the studant doesn't have any grades.
    # tranform zero in to one to avoid division by zero
    if count == 0:
        count += 1

    # return the average
    return average / count


def getPointsToBeAproved(grades: list[str]) -> float | int:
    """This function receives a list of grades from a studant and returns the points that he needs to pass the class"""

    pointsToPass = 0
    for i in range(len(grades)):
        # get the grades value from inside the table
        gradeValue = grades[i].find(attrs={"data-label": "Nota"})

        # Check if the grade is defined by the teacher, if not, don't count it
        if gradeValue.text.strip() == "-":
            pointsToPass += 0
        else:
            # Replace every comma with a dot and convert it to float then sum it to the rest of the grades
            pointsToPass += float(gradeValue.text.strip().replace(",", "."))

    # Calculate the points to pass, the minium grade is 18
    pointsToPass -= 18

    # Check if the points to pass is less than zero, if it is, it means that the studant already passed
    if pointsToPass > 0:
        pointsToPass = 0

    # Tranform the points to pass in a positive number
    return pointsToPass * -1


if __name__ == "__main__":
    print(verifyStudantInformation("123", "123"))
