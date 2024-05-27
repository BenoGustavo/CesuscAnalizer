# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectUserScreen.ui'
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
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from screens.resourcePath import resource_path


class Ui_SelectUserWindow(object):
    def setupUi(self, MainWindow): 
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 670)
        MainWindow.setMinimumSize(QSize(680, 670))
        MainWindow.setStyleSheet("background-color:#6E7DAB;")
        MainWindow.setWindowIcon(QIcon("assets/images/cesuscIcon.png"))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.frame.setMaximumSize(QSize(664, 600))
        self.frame.setStyleSheet("border-radius:50px;\n" "background-color:white;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tittleLabel = QLabel(self.frame)
        self.tittleLabel.setObjectName("tittleLabel")
        self.tittleLabel.setGeometry(QRect(60, 40, 521, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tittleLabel.setFont(font)
        self.tittleLabel.setStyleSheet("color:black;")
        self.tittleLabel.setAlignment(Qt.AlignCenter)  # Center the text

        self.subTittleLabel = QLabel(self.frame)
        self.subTittleLabel.setObjectName("subTittleLabel")
        self.subTittleLabel.setGeometry(QRect(60, 90, 451, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.subTittleLabel.setFont(font1)
        self.subTittleLabel.setStyleSheet("color:black;")
        self.subTittleLabel.setAlignment(Qt.AlignCenter)  # Center the text
        self.continueButton = QPushButton(self.frame)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setGeometry(QRect(60, 520, 201, 56))
        self.continueButton.setStyleSheet(
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
        self.registerButton = QPushButton(self.frame)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setGeometry(QRect(310, 520, 201, 56))
        self.registerButton.setStyleSheet(
            "QPushButton{\n"
            "	color:black;\n"
            "	background-color:#F39237;\n"
            "	border-radius:15px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color:#CB7A2F;\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color:#A56326;\n"
            "}"
        )
        self.usersFrame = QFrame(self.frame)
        self.usersFrame.setObjectName("usersFrame")
        self.usersFrame.setGeometry(QRect(60, 140, 551, 371))
        self.usersFrame.setFrameShape(QFrame.StyledPanel)
        self.usersFrame.setFrameShadow(QFrame.Raised)
        self.deleteUserButton = QPushButton(self.frame)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.deleteUserButton.setIcon(QIcon(resource_path("assets/images/garbage.png")))
        self.deleteUserButton.setIconSize(QSize(100, 100))  # set the size of the icon
        self.deleteUserButton.setGeometry(QRect(550, 520, 56, 56))
        self.deleteUserButton.setStyleSheet(
            "QPushButton{\n"
            "	background-color:#F15156;\n"
            "	border-radius:28px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color:rgb(196, 63, 68);\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color:rgb(121, 38, 40);\n"
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
        self.creditsLabel = QLabel(self.creditsFrame)
        self.creditsLabel.setObjectName("creditsLabel")
        font2 = QFont()
        font2.setPointSize(10)
        self.creditsLabel.setFont(font2)

        self.horizontalLayout_3.addWidget(self.creditsLabel, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.creditsFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Cesusc personal analyzer", None)
        )
        self.tittleLabel.setText(
            QCoreApplication.translate("MainWindow", "Selecione uma conta", None)
        )
        self.subTittleLabel.setText(
            QCoreApplication.translate(
                "MainWindow", "Bem vindo ao nosso analisador", None
            )
        )
        self.continueButton.setText(
            QCoreApplication.translate("MainWindow", "CONTINUAR", None)
        )
        self.registerButton.setText(
            QCoreApplication.translate("MainWindow", "REGISTRAR UMA CONTA", None)
        )
        self.creditsLabel.setText(
            QCoreApplication.translate(
                "MainWindow", "Created by Gustavo L. Gorges", None
            )
        )

    # retranslateUi
