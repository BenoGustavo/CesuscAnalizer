from PySide6.QtWidgets import QApplication
from screens.setupUIs import RegisterUserWindow, SelectUserWindow
from database.connection.studantController import studantsController

if __name__ == "__main__":
    database = studantsController()
    app = QApplication()
    window = RegisterUserWindow()
    window2 = SelectUserWindow()
    app.exec()
