from scraping.scrapper import verifyStudantInformation
from PySide6.QtCore import QObject, Signal


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
