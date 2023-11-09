from pathlib import Path
from os import path as systemPath
from os import mkdir


def isReportsDirCreated(filePath) -> bool:
    if systemPath.exists(filePath):
        return True
    return False


def createReportsDir(filePath):
    mkdir(filePath)


URL = "https://graduacao.cesusc.edu.br/projetos/nucleo/uteis/login.php?&tid=0&lid=0&pid=24&sid=98f8ec09184&&arq_ret=R5QT1WSRQBMCVQVPFFQSF99MCT5RT44Q9WRW0RBM0FMM5QQ4R4CV59RWRF1F5SWCW0"
# URL = "https://cesusc.edu.br/"


ROOT_PATH = Path(__file__).parent

CREDENCIALS_PATH = ROOT_PATH / ".credentials.json"

REPORTS_PATH = ROOT_PATH / "reports"

EXCEL_PATH = ROOT_PATH / "reports" / "Cesusc_Personal_info.xlsx"

WAITING_TIME = 5

if __name__ == "__main__":
    print(
        "ROOT DIR: " + str(ROOT_PATH),
    )
