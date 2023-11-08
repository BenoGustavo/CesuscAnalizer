from PySide6.QtWidgets import QMainWindow, QCheckBox, QVBoxLayout, QMessageBox
from screens.selectUserScreen import Ui_SelectUserWindow
from database.connection.studantController import studantsController
from PySide6.QtWidgets import QButtonGroup

"""This module is responsible for the select user window
All kinds of verification and database manipulation is done here"""


class SelectUserWindow(QMainWindow, Ui_SelectUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################

        self.selectedStudant: int = None

        self.configButtons()
        self.setStudantsInFrame()

        ############################
        self.show()

    def configButtons(self):
        self.registerButton.clicked.connect(self.registerButtonClicked)
        self.deleteUserButton.clicked.connect(self.deleteUserButtonClicked)

    def deleteUserButtonClicked(self):
        """This method is triggered by the delete user button

        It ask you if you are sure that you want to delete the user

        If you click Ok it will delete the user and show a message saying that the user was deleted

        If you click Cancel it will do nothing

        then it deletes the user from the database and updates the users in the frame"""

        if self.selectedStudant:
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
            studantsController().delete(self.selectedStudant)

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
                "Erro ao deletar usuário",
                QMessageBox.Icon.Information,
                "Ops! Nenhum usuário foi selecionado, selecione e tente novamente",
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
            self.selectedStudant = studant_id
            print(f"Checkbox for student {self.selectedStudant} is checked")
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
