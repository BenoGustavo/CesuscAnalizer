from browserInstance.makeChromeInstance import makeBrowser
from utils import URL

chromeBrowser = makeBrowser()
chromeBrowser.get(URL)
