# Window UI
from screens.registerScreen import Ui_RegisterUserWindow

# Database imports
from database.connection.studantController import studantsController
from database.studantModel import StudantModel

# Pyside6 imports
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QMessageBox

# Worker imports
from screens.controllers.workers import VerifyStudantInformationWorker

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

        # Trigger the worker and new threads to check if the user exists on cesusc, and don't crash the aplication
        self.__checkIfUserExistsOnCesusc()

        # clear all the fields
        self.usernameInput.clear()
        self.matriculaInput.clear()
        self.passwordInput.clear()

    def __checkIfUserExistsOnCesusc(self) -> bool:
        """This method creates a new thread and a new worker to check if the user exists on cesusc, it also connects the signals and slots

        This method deactivate the buttons while the worker is running and then activate them again when the worker finishes
        showing a message if the user was created or not
        """

        # create a new thread and a new worker
        self.thread = QThread()
        self.worker = VerifyStudantInformationWorker(
            self.enrollment_number, self.password
        )

        # connect the signals and slots
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.thread.quit)

        # delete the thread and the worker when they finish
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        # Change the button stylesheets and disable them while the worker is running
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

        # When the worker finishes, it will trigger this function
        self.worker.finished.connect(self.workerFinished)

        self.thread.start()

        self.showErrorMessage(
            "Estamos verificando suas informações, por favor aguarde",
            QMessageBox.Icon.Information,
            "Verificando informações",
        )

    def workerFinished(self, isStudantCredentialsValid: bool):
        """This method is triggered when the worker finishes, it gets the result from the worker quary and
        then decideses if the user will be create it in the database"""

        if not isStudantCredentialsValid:
            self.showErrorMessage(
                "Sua matrícula ou senha incorretos",
                QMessageBox.Icon.Warning,
                "Falha ao registrar usuário",
            )

            # Return the stylesheets to the original and enable the buttons
            self.returnButton.setStyleSheet(self.__returnBtnStylesheet)
            self.registerButton.setStyleSheet(self.__registerBtnStylesheet)
            self.returnButton.setEnabled(True)
            self.registerButton.setEnabled(True)

            # Do and early return because the user doesn't exists
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

        # Return the stylesheets to the original and enable the buttons
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
