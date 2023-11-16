# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerUserScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_RegisterUserWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 752)
        MainWindow.setMinimumSize(QSize(674, 660))
        MainWindow.setStyleSheet("background-color:#6E7DAB;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.returnBtnFrame = QFrame(self.centralwidget)
        self.returnBtnFrame.setObjectName("returnBtnFrame")
        self.returnBtnFrame.setMinimumSize(QSize(0, 0))
        self.returnBtnFrame.setMaximumSize(QSize(16777215, 85))
        self.returnBtnFrame.setStyleSheet("")
        self.returnBtnFrame.setFrameShape(QFrame.NoFrame)
        self.returnBtnFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.returnBtnFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.returnButton = QPushButton(self.returnBtnFrame)
        self.returnButton.setObjectName("returnButton")
        self.returnButton.setMinimumSize(QSize(60, 60))
        self.returnButton.setIcon(QIcon("assets/images/returnArrow.png"))
        self.returnButton.setIconSize(QSize(25, 25))  # set the size of the icon
        self.returnButton.setStyleSheet(
            "QPushButton{\n"
            "	border-radius:30px;\n"
            "	background-color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color:rgb(206, 206, 206);\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	border:2px solid #6E7DAB;\n"
            "	background-color:rgb(156, 156, 156);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.returnButton, 0, Qt.AlignLeft)

        self.verticalLayout.addWidget(self.returnBtnFrame)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName("mainFrame")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.mainFrame)
        self.frame.setObjectName("frame")
        self.frame.setMaximumSize(QSize(664, 561))
        self.frame.setStyleSheet("border-radius:50px;\n" "background-color:white;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tittleLabel = QLabel(self.frame)
        self.tittleLabel.setObjectName("tittleLabel")
        self.tittleLabel.setGeometry(QRect(60, 60, 301, 41))
        font = QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.tittleLabel.setFont(font)
        self.tittleLabel.setStyleSheet("color:black;")
        self.subTittleLabel = QLabel(self.frame)
        self.subTittleLabel.setObjectName("subTittleLabel")
        self.subTittleLabel.setGeometry(QRect(60, 100, 371, 41))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.subTittleLabel.setFont(font1)
        self.subTittleLabel.setStyleSheet("color:black;")
        self.usernameInput = QLineEdit(self.frame)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameInput.setGeometry(QRect(60, 200, 546, 56))
        self.usernameInput.setStyleSheet(
            "QLineEdit{\n"
            "	background-color: #D9D9D9;\n"
            "	border-radius:15px;\n"
            "	color:rgb(94, 92, 100);\n"
            "	padding-left:15px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus{\n"
            "	border: 2px solid #6E7DAB;\n"
            "}"
        )
        self.usernameInput.setMaxLength(50)
        self.matriculaInput = QLineEdit(self.frame)
        self.matriculaInput.setObjectName("matriculaInput")
        self.matriculaInput.setGeometry(QRect(60, 280, 546, 56))
        self.matriculaInput.setStyleSheet(
            "QLineEdit{\n"
            "	background-color: #D9D9D9;\n"
            "	border-radius:15px;\n"
            "	color:rgb(94, 92, 100);\n"
            "	padding-left:15px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus{\n"
            "	border: 2px solid #6E7DAB;\n"
            "}"
        )
        self.matriculaInput.setMaxLength(50)
        self.passwordInput = QLineEdit(self.frame)
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setGeometry(QRect(60, 360, 546, 56))
        self.passwordInput.setStyleSheet(
            "QLineEdit{\n"
            "	background-color: #D9D9D9;\n"
            "	border-radius:15px;\n"
            "	color:rgb(94, 92, 100);\n"
            "	padding-left:15px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus{\n"
            "	border: 2px solid #6E7DAB;\n"
            "}"
        )
        self.passwordInput.setMaxLength(50)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.registerButton = QPushButton(self.frame)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setGeometry(QRect(160, 470, 324, 56))
        self.registerButton.setStyleSheet(
            "QPushButton{\n"
            "	color:black;\n"
            "	background-color:#A8B4A5;\n"
            "	border-radius:15px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color:rgb(117, 129, 114);\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color:rgb(82, 88, 80);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.frame)

        self.verticalLayout.addWidget(self.mainFrame)

        self.creditsFrame = QFrame(self.centralwidget)
        self.creditsFrame.setObjectName("creditsFrame")
        self.creditsFrame.setMaximumSize(QSize(16777215, 30))
        self.creditsFrame.setFrameShape(QFrame.NoFrame)
        self.creditsFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.creditsFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.credits_label = QLabel(self.creditsFrame)
        self.credits_label.setObjectName("credits_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.credits_label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.credits_label, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.creditsFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Cesusc personal analyzer", None)
        )
        self.returnButton.setText("")
        self.tittleLabel.setText(
            QCoreApplication.translate("MainWindow", "REGISTRAR", None)
        )
        self.subTittleLabel.setText(
            QCoreApplication.translate("MainWindow", "Registrar uma nova conta", None)
        )
        self.usernameInput.setText("")
        self.usernameInput.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Insira aqui seu nome", None)
        )
        self.matriculaInput.setText("")
        self.matriculaInput.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Insira aqui a sua matr\u00edcula", None
            )
        )
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Insira aqui a sua senha", None)
        )
        self.registerButton.setText(
            QCoreApplication.translate("MainWindow", "REGISTAR NOVA CONTA", None)
        )
        self.credits_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Created by Gustavo L. Gorges", None
            )
        )

    # retranslateUi
