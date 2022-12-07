from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(125, 41, 311, 221))
        self.textInput.setObjectName("textInput")
        self.useGPU = QtWidgets.QCheckBox(self.centralwidget)
        self.useGPU.setGeometry(QtCore.QRect(10, 350, 261, 22))
        self.useGPU.setObjectName("useGPU")
        self.runButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.runButton.setEnabled(False)
        self.runButton.setGeometry(QtCore.QRect(10, 300, 168, 41))
        self.runButton.setObjectName("runButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(333, 320, 101, 34))
        self.saveButton.setObjectName("saveButton")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        self.playButton.setGeometry(QtCore.QRect(333, 370, 101, 34))
        self.playButton.setObjectName("playButton")
        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(10, 398, 541, 20))
        self.statusBar.setObjectName("statusBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.useGPU.setText(_translate("MainWindow", "Использовать расчёты на видеокарте"))
        self.runButton.setText(_translate("MainWindow", "Озвучить"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.playButton.setText(_translate("MainWindow", "Послушать"))
        self.statusBar.setText(_translate("MainWindow", "Готово к работе"))
