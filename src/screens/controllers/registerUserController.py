from PySide6.QtWidgets import QMainWindow, QMessageBox
from screens.registerScreen import Ui_RegisterUserWindow
from database.connection.studantController import studantsController
from database.studantModel import StudantModel
from PySide6.QtGui import QRegularExpressionValidator

"""This module is responsible for the register user window
All kinds of verification and database manipulation is done here"""


class RegisterUserWindow(QMainWindow, Ui_RegisterUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################

        self.__ONLY_LETTERS_REGEX = QRegularExpressionValidator("[a-zA-Z]+")
        self.__ONLY_NUMBBER_REGEX = QRegularExpressionValidator("[0-9]+")

        self.__configButtons()

        self.__inputsValidation()

        ############################

        self.show()

    def __configButtons(self):
        """Configure all the buttons in the screen with their respective functions"""

        self.returnButton.clicked.connect(self.returnButtonClicked)
        self.registerButton.clicked.connect(self.registerButtonClicked)

    def __inputsValidation(self):
        """This method validates all the inputs in the screen"""

        # Validate the username input
        self.usernameInput.setValidator(self.__ONLY_LETTERS_REGEX)
        # Validate the matricula input
        self.matriculaInput.setValidator(self.__ONLY_NUMBBER_REGEX)

    def registerButtonClicked(self):
        """This method is triggered by the register button, it creates a new user in the database

        First it checks if all the fields are filled, if not it shows an error message

        Then it creates a new user in the database and shows a message saying that the user was created

        Then it clears all the fields"""

        # Check if all fields are filled
        if (
            self.usernameInput.isModified() == False
            or self.matriculaInput.isModified() == False
            or self.passwordInput.isModified() == False
        ):
            # show the popup if needed
            self.__showErrorMessage(
                "Preencha todos os campos",
                QMessageBox.Icon.Warning,
                "Ops! Os campos não foram preenchidos",
            )
            return

        # get the text from the inputs
        username = self.usernameInput.text()
        enrollment_number = self.matriculaInput.text()
        password = self.passwordInput.text()

        # create a new user from the studant model and then create it in the database
        newStudant = StudantModel(username, enrollment_number, password)
        studantsController().create(newStudant)

        # show the popup saying that the user was created
        self.__showErrorMessage(
            "Usuário registrado com sucesso!",
            QMessageBox.Icon.Information,
            "Usuário registrado",
        )

        # clear all the fields
        self.usernameInput.clear()
        self.matriculaInput.clear()
        self.passwordInput.clear()

    def returnButtonClicked(self):
        """This method is triggered by the return button, it hides the current window and shows the select user window"""
        self.hide()

        # import the select user window here to avoid circular imports########
        from screens.controllers.selectUserController import SelectUserWindow  #

        ##################################################

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
