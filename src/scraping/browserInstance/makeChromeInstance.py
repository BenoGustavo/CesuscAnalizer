from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from get_chrome_driver import GetChromeDriver

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

from sys import platform
from pathlib import Path

ROOT_PATH = Path(__file__).parent

UNIX_SYSTEMS = ["linux", "linux2", "darwin"]
# if the platform is a unix based system
if platform in UNIX_SYSTEMS:
    CHROME_DRIVER_PATH = ROOT_PATH / "bin" / "chromedriver"
# else is windows
else:
    CHROME_DRIVER_PATH = ROOT_PATH / "bin" / "chromedriver.exe"


def makeBrowser(*options: str) -> webdriver.Chrome:
    # check the version of the chromedriver and download the latest version
    get_driver = GetChromeDriver()
    get_driver.install(output_path=str(CHROME_DRIVER_PATH.parent))

    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.set_window_size(1200, 700)

    return browser
