# Ui imports
from screens.selectUserScreen import Ui_SelectUserWindow

# Database imports
from database.connection.studantController import studantsController

# Pyside6 imports
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QButtonGroup
from PySide6.QtWidgets import QMainWindow, QCheckBox, QVBoxLayout, QMessageBox

# Worker imports
from screens.controllers.workers import CesuscScrapperWorker

"""This module is responsible for the select user window
All kinds of verification and database manipulation is done here"""


class SelectUserWindow(QMainWindow, Ui_SelectUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################
        self.__continueButtonStyleSheet = self.continueButton.styleSheet()
        self.__registerButtonStyleSheet = self.registerButton.styleSheet()

        self.selectedStudantId: int = None

        self.configButtons()
        self.setStudantsInFrame()

        ############################
        self.show()

    def configButtons(self):
        self.continueButton.clicked.connect(self.continueButtonClicked)
        self.registerButton.clicked.connect(self.registerButtonClicked)
        self.deleteUserButton.clicked.connect(self.deleteUserButtonClicked)

    def continueButtonClicked(self):
        """This method do the scrapping for the selected user"""

        if self.selectedStudantId:
            # Create a pop up asking if the user is sure that he wants to delete the user
            userChoice = self.__showMessagePopUp(
                "Esse processo pode demorar um pouco dependo da maquina em que está sendo executada",
                QMessageBox.Icon.Warning,
                "Tem certeza que deseja realizar a consulta?",
                True,
            )

            # Return if the user clicked cancel
            if userChoice != QMessageBox.Ok:
                return

            # Get the user data from the database to use in to the scrappping
            userData = studantsController().getStudant(self.selectedStudantId)

            self.continueButton.setText("Consultando...")
            self.continueButton.setDisabled(True)

            # Create a scrapper instance
            self.makeScrapper(userData[1], userData[2], userData[3])

            self.continueButton.setText("Continuar")
            self.continueButton.setDisabled(False)

        else:
            self.__showMessagePopUp(
                "Ops! Nenhum usuário foi selecionado, selecione e tente novamente",
                QMessageBox.Icon.Information,
                "Erro ao realizar consulta de informações escolares",
                True,
            )

    def makeScrapper(self, username: str, password: str, registrationNumber: str):
        """This method creates a new thread and a new worker to get the subjects data from cesusc website, it also connects the signals and slots

        This method deactivate the buttons while the worker is running and then activate them again when the worker finishes
        showing a feedback message
        """

        # create a new thread and a new worker
        self.thread = QThread()
        self.worker = CesuscScrapperWorker(username, password, registrationNumber)

        # connect the signals and slots
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        # delete the thread and the worker when they finish
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        # Change the button stylesheets and disable them while the worker is running
        self.worker.started.connect(
            lambda: (
                self.continueButton.setEnabled(False),
                self.continueButton.setStyleSheet(
                    "border-radius:15px;color:black;background-color:rgb(82, 88, 80);"
                ),
                self.registerButton.setEnabled(False),
                self.registerButton.setStyleSheet(
                    "border-radius:15px;color:black;background-color:#A56326;"
                ),
            )
        )

        # When the worker finishes, it will trigger this function
        self.worker.finished.connect(self.workerFinished)

        self.thread.start()

    def workerFinished(self):
        """This method is triggered when the worker finishes, it restores the buttons to the original state"""

        self.continueButton.setStyleSheet(self.__continueButtonStyleSheet)
        self.continueButton.setEnabled(True)

        self.registerButton.setStyleSheet(self.__registerButtonStyleSheet)
        self.registerButton.setEnabled(True)

        # Creates a message saying that the worker finished
        self.__showMessagePopUp(
            "A consulta foi realizada com sucesso!\n\nSeu arquivo pode ser encontrado dentro da raiz do programa na pasta 'out'",
            QMessageBox.Icon.Information,
            "Consulta realizada",
            True,
        )

    def deleteUserButtonClicked(self):
        """This method is triggered by the delete user button

        It ask you if you are sure that you want to delete the user

        If you click Ok it will delete the user and show a message saying that the user was deleted

        If you click Cancel it will do nothing

        then it deletes the user from the database and updates the users in the frame"""

        if self.selectedStudantId:
            # Create a pop up asking if the user is sure that he wants to delete the user
            userChoice = self.__showMessagePopUp(
                "Tem certeza que deseja deletar o usuário?",
                QMessageBox.Icon.Warning,
                "Deletar usuário",
            )

            # Return if the user clicked cancel
            if userChoice != QMessageBox.Ok:
                return

            # deletes the user from the database
            studantsController().delete(self.selectedStudantId)

            # Show a message saying that the user was deleted
            self.__showMessagePopUp(
                "Usuário deletado com sucesso!",
                QMessageBox.Icon.Information,
                "Usuário deletado",
                True,
            )

            # Update the users in the frame
            self.updateStudantsInFrame()
        else:
            self.__showMessagePopUp(
                "Ops! Nenhum usuário foi selecionado, selecione e tente novamente",
                QMessageBox.Icon.Information,
                "Erro ao deletar usuário",
                False,
            )

    def updateStudantsInFrame(self):
        """This method basicly deletes all checkboxes and then creates them again"""

        # iterate over all children of the frame and delete them if they are checkboxes
        for child in self.usersFrame.children():
            if isinstance(child, QCheckBox):
                child.deleteLater()

        # Create the checkboxes again
        self.setStudantsInFrame()

    def setStudantsInFrame(self):
        """This method creates a checkbox for each user in the database and adds it to the frame

        It also creates a button group to make sure that only one checkbox is checked at a time
        """

        # Get all studants from the database
        studants = studantsController().getStudants()

        # Create a button group and set it to be exclusive
        checkboxGroup = QButtonGroup(self)
        checkboxGroup.setExclusive(True)

        # Set the layout type
        self.usersFrame.setLayout(QVBoxLayout())

        # Iterate over all studants and create a checkbox for each one
        for studant in studants:
            studantCheckBox = QCheckBox(studant[1])
            studantCheckBox.setObjectName(studant[1] + "CheckBox")
            studantCheckBox.setStyleSheet("color:black;font-size:24px;")

            # Use a lambda function to pass the student id when the checkbox is clicked
            studantCheckBox.clicked.connect(
                self.createCheckboxClickedLambda(studant, studantCheckBox)
            )

            # Add the current checkbox to the group
            checkboxGroup.addButton(studantCheckBox)

            # Add the checkbox to the frame
            self.usersFrame.layout().addWidget(studantCheckBox)

    # This method is used to create a lambda function that passes the studant id when the checkbox is clicked
    def createCheckboxClickedLambda(self, studant, studantCheckBox):
        return lambda: self.checkboxClicked(studantCheckBox.isChecked(), studant[0])

    def checkboxClicked(self, checked, studant_id):
        """this method is triggered when a checkbox is clicked and don't should be used for anything else

        It just sets the selectedStudant variable to the id of the studant that was clicked
        """
        if checked:
            self.selectedStudantId = studant_id
            print(f"Checkbox for student {self.selectedStudantId} is checked")
        else:
            print(f"Checkbox for student {studant_id} is unchecked")

    def registerButtonClicked(self):
        """This method trigger the register user screen"""
        self.hide()

        # This import is here to avoid circular imports######################
        from screens.controllers.registerUserController import RegisterUserWindow  #

        ######################################################

        self.registerWindow = RegisterUserWindow()
        self.registerWindow.show()

    def __showMessagePopUp(
        self,
        message: str,
        icon: QMessageBox.Icon,
        title: str,
        isInformative: bool = False,
    ) -> int:
        """This method creates a QMessageBox with the given parameters and then execute it"""
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)

        if isInformative:
            msgBox.setStandardButtons(QMessageBox.Ok)
        else:
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        return msgBox.exec()
