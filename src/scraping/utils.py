from pathlib import Path
from os import path as systemPath
from os import mkdir


def isReportsDirCreated(filePath) -> bool:
    if systemPath.exists(filePath):
        return True
    return False


def createReportsDir(filePath):
    mkdir(filePath)


URL = "https://cesusc.edu.br/"


ROOT_PATH = Path(__file__).parent

CREDENCIALS_PATH = ROOT_PATH / ".credentials.json"

REPORTS_PATH = ROOT_PATH / "reports"

EXCEL_PATH = ROOT_PATH / "reports" / "Cesusc_Personal_info.xlsx"

WAITING_TIME = 5

if __name__ == "__main__":
    print(
        "ROOT DIR: " + str(ROOT_PATH),
    )
