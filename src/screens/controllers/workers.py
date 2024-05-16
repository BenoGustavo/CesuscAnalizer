from scraping.scrapper import verifyStudantInformation, Scrapper


class CesuscScrapperWorker:

    def __init__(
        self,
        username: str,
        enrollment_number: str,
        password: str,
    ) -> None:
        self.username = username
        self.enrollment_number = enrollment_number
        self.password = password

    def run(self):
        scrapperInstance = Scrapper(
            self.username, self.enrollment_number, self.password
        )


class VerifyStudantInformationWorker:
    def __init__(
        self,
        enrollment_number,
        password,
    ) -> None:

        self.enrollment_number = enrollment_number
        self.password = password

    def run(self):
        result = verifyStudantInformation(self.enrollment_number, self.password)
