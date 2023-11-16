from scraping.scrapper import verifyStudantInformation, Scrapper
from PySide6.QtCore import QObject, Signal


class CesuscScrapperWorker(QObject):
    started = Signal()
    finished = Signal()

    def __init__(
        self,
        username: str,
        enrollment_number: str,
        password: str,
        parent: QObject = None,
    ) -> None:
        super().__init__(parent)
        self.username = username
        self.enrollment_number = enrollment_number
        self.password = password

    def run(self):
        self.started.emit()

        scrapperInstance = Scrapper(
            self.username, self.enrollment_number, self.password
        )

        self.finished.emit()


class VerifyStudantInformationWorker(QObject):
    started = Signal()
    finished = Signal(bool)

    def __init__(
        self,
        enrollment_number,
        password,
        parent: QObject = None,
    ) -> None:
        super().__init__(parent)
        self.enrollment_number = enrollment_number
        self.password = password

    def run(self):
        self.started.emit()

        result = verifyStudantInformation(self.enrollment_number, self.password)

        self.finished.emit(result)
