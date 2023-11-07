from PySide6.QtWidgets import QMainWindow
from screens.selectUserScreen import Ui_SelectUserWindow
from screens.registerScreen import Ui_RegisterUserWindow


class SelectUserWindow(QMainWindow, Ui_SelectUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()


class RegisterUserWindow(QMainWindow, Ui_RegisterUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
