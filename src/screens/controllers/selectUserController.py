from PySide6.QtWidgets import QMainWindow, QCheckBox, QVBoxLayout
from screens.selectUserScreen import Ui_SelectUserWindow
from database.connection.studantController import studantsController
from PySide6.QtWidgets import QButtonGroup


class SelectUserWindow(QMainWindow, Ui_SelectUserWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        ############################

        self.configButtons()
        self.setStudantsInFrame()

        ############################
        self.show()

    def configButtons(self):
        self.registerButton.clicked.connect(self.registerButtonClicked)

    def setStudantsInFrame(self):
        studants = studantsController().getStudants()
        button_group = QButtonGroup(self)
        button_group.setExclusive(True)

        for studant in studants:
            studantCheckBox = QCheckBox(studant[1])
            studantCheckBox.setObjectName(studant[1] + "CheckBox")
            studantCheckBox.setStyleSheet("color:black;font-size:24px;")

            # Use a lambda function to pass the student id when the checkbox is clicked
            studantCheckBox.clicked.connect(
                self.createCheckboxClickedLambda(studant, studantCheckBox)
            )

            button_group.addButton(studantCheckBox)

            self.usersFrame.setLayout(QVBoxLayout())
            self.usersFrame.layout().addWidget(studantCheckBox)

    def createCheckboxClickedLambda(self, studant, studantCheckBox):
        return lambda: self.checkboxClicked(studantCheckBox.isChecked(), studant[0])

    def checkboxClicked(self, checked, studant_id):
        if checked:
            print(f"Checkbox for student {studant_id} is checked")
        else:
            print(f"Checkbox for student {studant_id} is unchecked")

    def registerButtonClicked(self):
        self.hide()
        from screens.controllers.registerUserController import RegisterUserWindow

        self.registerWindow = RegisterUserWindow()
        self.registerWindow.show()
