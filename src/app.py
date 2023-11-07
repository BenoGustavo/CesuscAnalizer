from PySide6.QtWidgets import QApplication
from screens.controllers.selectUserController import SelectUserWindow
from database.connection.studantController import studantsController

if __name__ == "__main__":
    database = studantsController()
    app = QApplication()
    window = SelectUserWindow()
    app.exec()
