from scraping.browserInstance.makeChromeInstance import makeBrowser
from scraping.utils import URL, WAITING_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


def verifyStudantInformation(registrationNumber: str, password: str):
    """Get the info from the studant from registerUserController and verify if the user exists

    RETURNS: True if the user exists and False if not
    """

    # Create a browser instance
    chromeBrowser = makeBrowser("--headless")
    chromeBrowser.get(URL)

    # wait until the sistema-academico button is loaded then click on the button to open the login form
    # academicSystem = chromeBrowser.find_element(By.CLASS_NAME, "sistema-academico")
    # academicSystem.click()

    # List of all opened tabs
    # openTabs = chromeBrowser.window_handles
    # Picking the new tab opened
    # academicSystemTab = openTabs[-1]

    # Changing it on browser
    # chromeBrowser.switch_to.window(academicSystemTab)

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


if __name__ == "__main__":
    print(verifyStudantInformation("123", "123"))
