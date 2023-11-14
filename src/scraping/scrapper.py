from scraping.browserInstance.makeChromeInstance import makeBrowser
from scraping.utils import URL, WAITING_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


def verifyStudantInformation(registrationNumber: str, password: str) -> bool:
    """Get the info from the studant from registerUserController and verify if the user exists

    RETURNS: True if the user exists and False if not
    """

    # Create a browser instance
    chromeBrowser = makeBrowser("--headless")
    chromeBrowser.get(URL)

    ####################################################################
    #######################old-code-using-other-url#############################

    # wait until the sistema-academico button is loaded then click on the button to open the login form
    # academicSystem = chromeBrowser.find_element(By.CLASS_NAME, "sistema-academico")
    # academicSystem.click()

    # List of all opened tabs
    # openTabs = chromeBrowser.window_handles
    # Picking the new tab opened
    # academicSystemTab = openTabs[-1]

    # Changing it on browser
    # chromeBrowser.switch_to.window(academicSystemTab)

    ####################################################################
    #########################old-code-using-other-url###########################

    # Getting the inputs from the login form

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
    def __init__(self, registrationNumber: str, password: str) -> None:
        self.subjectNamesList = []
        self.subjectPagesHtml = []

        # Create a browser instance
        self.chromeBrowser = makeBrowser()
        self.chromeBrowser.get(URL)

        self.loginCesuscWebsite(registrationNumber, password)
        self.acessingGradesAndFrequency()
        self.settingIframeToChromeDriver()
        self.getSubjectsNames()
        self.getSubjectPagesHtml()

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

        # Click on the grades and frequency button
        gradesAndFrequencyButton[6].click()

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
        # Wait for the table to be fully loaded and select it
        table = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@class='slim highlight']")
            )
        )

        # Get the table of the subjects using xpath
        subjectsRows = table.find_elements(By.TAG_NAME, "tr")

        # Getting the first row with the name of the subects
        subjectsRows = subjectsRows[0].find_elements(By.TAG_NAME, "tr")

        # Appeding the subject names to the list skiping the first row because it's the header
        for i in range(1, len(subjectsRows)):
            self.subjectNamesList.append(subjectsRows[i].text)

    def getSubjectPagesHtml(self) -> None:
        # Wait for the table to be fully loaded and select it
        table = WebDriverWait(self.chromeBrowser, WAITING_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@class='slim highlight']")
            )
        )

        # Get the table of the subjects using xpath
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

                subjectsRows = subjectsRows[0].find_elements(By.TAG_NAME, "tr")

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


if __name__ == "__main__":
    print(verifyStudantInformation("123", "123"))
