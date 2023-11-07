from dataclasses import dataclass


@dataclass
class StudantModel:
    id: int
    username: str
    enrollment_number: int
    password: str

    studantsList = []

    def __init__(self, username, enrollment_number, password, id=None):
        self.id = id
        self.username = username
        self.enrollment_number = enrollment_number
        self.password = password

    def addStudant(self, studant):
        """Add a studantModel to the studantsList"""
        self.studantsList.append(studant)
