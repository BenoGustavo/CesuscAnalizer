from PySide6.QtWidgets import QMainWindow, QMessageBox
from screens.registerScreen import Ui_RegisterUserWindow
from database.connection.studantController import studantsController
from database.studantModel import StudantModel


class RegisterUserWindow(QMainWindow, Ui_RegisterUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################

        self.configButtons()

        ############################

        self.show()

    def configButtons(self):
        self.returnButton.clicked.connect(self.returnButtonClicked)
        self.registerButton.clicked.connect(self.registerButtonClicked)

    def registerButtonClicked(self):
        # Check if all fields are filled
        if (
            self.usernameInput.isModified() == False
            or self.matriculaInput.isModified() == False
            or self.passwordInput.isModified() == False
        ):
            self.__showErrorMessage(
                "Preencha todos os campos",
                QMessageBox.Icon.Warning,
                "Ops! Os campos não foram preenchidos",
            )
            return

        username = self.usernameInput.text()
        enrollment_number = self.matriculaInput.text()
        password = self.passwordInput.text()

        newStudant = StudantModel(username, enrollment_number, password)
        studantsController().create(newStudant)

        self.__showErrorMessage(
            "Usuário registrado com sucesso!",
            QMessageBox.Icon.Information,
            "Usuário registrado",
        )

    def returnButtonClicked(self):
        self.hide()
        from screens.controllers.selectUserController import SelectUserWindow

        self.selectUserWindow = SelectUserWindow()
        self.selectUserWindow.show()

    def __showErrorMessage(
        self, message: str, icon: QMessageBox.Icon, title: str
    ) -> None:
        """This method creates a QMessageBox with the given parameters and then execute it"""
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)

        msgBox.setStandardButtons(QMessageBox.Ok)

        msgBox.exec()
