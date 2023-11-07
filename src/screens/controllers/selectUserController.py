from PySide6.QtWidgets import QMainWindow
from screens.selectUserScreen import Ui_SelectUserWindow


class SelectUserWindow(QMainWindow, Ui_SelectUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################

        self.configButtons()

        ############################
        self.show()

    def configButtons(self):
        self.registerButton.clicked.connect(self.registerButtonClicked)

    def registerButtonClicked(self):
        self.hide()
        from screens.controllers.registerUserController import RegisterUserWindow

        self.registerWindow = RegisterUserWindow()
        self.registerWindow.show()
