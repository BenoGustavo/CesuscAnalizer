from PySide6.QtWidgets import QMainWindow, QMessageBox
from screens.registerScreen import Ui_RegisterUserWindow
from database.connection.studantController import studantsController
from database.studantModel import StudantModel
from PySide6.QtGui import QRegularExpressionValidator
from scraping.scrapper import verifyStudantInformation
from PySide6.QtCore import QObject, Signal, QThread

"""This module is responsible for the register user window
All kinds of verification and database manipulation is done here"""


class RegisterUserWindow(QMainWindow, Ui_RegisterUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################
        self.__registerBtnStylesheet = self.registerButton.styleSheet()
        self.__returnBtnStylesheet = self.returnButton.styleSheet()

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
            self.showErrorMessage(
                "Preencha todos os campos",
                QMessageBox.Icon.Warning,
                "Ops! Os campos não foram preenchidos",
            )
            return

        # get the text from the inputs
        self.username = self.usernameInput.text()
        self.enrollment_number = self.matriculaInput.text()
        self.password = self.passwordInput.text()

        self.checkIfUserExistsOnCesusc()

        # clear all the fields
        self.usernameInput.clear()
        self.matriculaInput.clear()
        self.passwordInput.clear()

    def checkIfUserExistsOnCesusc(self) -> bool:
        # create a new thread to create the user in the database and checks if the user exists
        self.thread = QThread()
        self.worker = Worker(self.enrollment_number, self.password)

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.thread.quit)

        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        self.worker.started.connect(
            lambda: (
                self.registerButton.setEnabled(False),
                self.registerButton.setStyleSheet(
                    "border-radius:15px;color:black;background-color:rgb(82, 88, 80);"
                ),
                self.returnButton.setEnabled(False),
                self.returnButton.setStyleSheet(
                    "border-radius:30px;border:2px solid #6E7DAB; background-color:rgb(156, 156, 156);"
                ),
            )
        )
        self.worker.finished.connect(self.workerFinished)

        self.thread.start()

        self.showErrorMessage(
            "Estamos verificando suas informações, por favor aguarde",
            QMessageBox.Icon.Information,
            "Verificando informações",
        )

    def workerFinished(self, isStudantCredentialsValid: bool):
        if not isStudantCredentialsValid:
            self.showErrorMessage(
                "Sua matrícula ou senha incorretos",
                QMessageBox.Icon.Warning,
                "Falha ao registrar usuário",
            )

            self.returnButton.setStyleSheet(self.__returnBtnStylesheet)
            self.registerButton.setStyleSheet(self.__registerBtnStylesheet)

            self.returnButton.setEnabled(True)
            self.registerButton.setEnabled(True)
            return

        # create a new user from the studant model and then create it in the database
        newStudant = StudantModel(self.username, self.enrollment_number, self.password)
        studantsController().create(newStudant)

        # show the popup saying that the user was created
        self.showErrorMessage(
            "Usuário registrado com sucesso!",
            QMessageBox.Icon.Information,
            "Usuário registrado",
        )

        self.returnButton.setStyleSheet(self.__returnBtnStylesheet)
        self.registerButton.setStyleSheet(self.__registerBtnStylesheet)

        self.returnButton.setEnabled(True)
        self.registerButton.setEnabled(True)

    def returnButtonClicked(self):
        """This method is triggered by the return button, it hides the current window and shows the select user window"""
        self.hide()

        # import the select user window here to avoid circular imports########
        from screens.controllers.selectUserController import SelectUserWindow  #

        ##################################################

        self.selectUserWindow = SelectUserWindow()
        self.selectUserWindow.show()

    def showErrorMessage(
        self, message: str, icon: QMessageBox.Icon, title: str
    ) -> None:
        """This method creates a QMessageBox with the given parameters and then execute it"""
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)

        msgBox.setStandardButtons(QMessageBox.Ok)

        msgBox.exec()


class Worker(QObject):
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
