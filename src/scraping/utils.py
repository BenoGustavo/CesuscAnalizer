from pathlib import Path
from os import path as systemPath
from os import makedirs
from datetime import datetime


def getCurrentTime() -> str:
    # get current date and time
    now = datetime.now()
    current_time = now.strftime("%d|%m|%Y - %H;%M")

    return current_time


def isFileCreated(filePath) -> bool:
    if systemPath.exists(filePath):
        return True
    return False


def createReportsDir(filePath) -> None:
    makedirs(filePath)


URL = "https://graduacao.cesusc.edu.br/projetos/nucleo/uteis/login.php?&tid=0&lid=0&pid=24&sid=98f8ec09184&&arq_ret=R5QT1WSRQBMCVQVPFFQSF99MCT5RT44Q9WRW0RBM0FMM5QQ4R4CV59RWRF1F5SWCW0"

# Write headers to the worksheet
XLSX_HEADERS = [
    "Nome da Materia",
    "N1 - Dia da prova",
    "N1 - Nota",
    "N2 - Dia da prova",
    "N2 - Nota",
    "N3 - Dia da prova",
    "N3 - Nota",
    "Media da materia",
    "Pontos para aprovaçao",
    "Maximo de faltas",
    "Suas Faltas",
    "Quanto ainda pode ser faltado",
    "Frequencia em %",
]

ROOT_PATH = Path(__file__).parent.parent.parent

CREDENCIALS_PATH = ROOT_PATH / ".credentials.json"

getReportsPath = lambda username: ROOT_PATH / "out" / "reports" / username


getExcelPath = lambda REPORTS_PATH: REPORTS_PATH / "Cesusc_Info.xlsx"


WAITING_TIME = 5

if __name__ == "__main__":
    print(
        "ROOT DIR: " + str(ROOT_PATH),
    )
