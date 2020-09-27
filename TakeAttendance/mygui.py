# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QListWidgetItem
from TakeAttendance.FaceScanner import *
from TakeAttendance.DataSet import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.path_box = QtWidgets.QLineEdit(self.centralwidget)
        self.path_box.setGeometry(QtCore.QRect(30, 40, 401, 31))
        self.path_box.setObjectName("path_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selectDir_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectDir_button.setGeometry(QtCore.QRect(490, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectDir_button.setFont(font)
        self.selectDir_button.setObjectName("selectDir_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.addNewPerson_button = QtWidgets.QPushButton(self.centralwidget)
        self.addNewPerson_button.setGeometry(QtCore.QRect(320, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addNewPerson_button.setFont(font)
        self.addNewPerson_button.setObjectName("addNewPerson_button")
        self.personName_box = QtWidgets.QLineEdit(self.centralwidget)
        self.personName_box.setGeometry(QtCore.QRect(400, 270, 181, 22))
        self.personName_box.setObjectName("personName_box")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 270, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.train_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_button.setGeometry(QtCore.QRect(30, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.train_button.setFont(font)
        self.train_button.setObjectName("train_button")
        self.workingPath_box = QtWidgets.QLineEdit(self.centralwidget)
        self.workingPath_box.setGeometry(QtCore.QRect(140, 90, 291, 31))
        self.workingPath_box.setObjectName("workingPath_box")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.selectNewDir_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectNewDir_button.setGeometry(QtCore.QRect(490, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectNewDir_button.setFont(font)
        self.selectNewDir_button.setObjectName("selectNewDir_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 130, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.findPeople_button = QtWidgets.QPushButton(self.centralwidget)
        self.findPeople_button.setGeometry(QtCore.QRect(30, 177, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.findPeople_button.setFont(font)
        self.findPeople_button.setObjectName("findPeople_button")
        self.person_list = QtWidgets.QListWidget(self.centralwidget)
        self.person_list.setGeometry(QtCore.QRect(40, 270, 256, 192))
        self.person_list.setObjectName("person_list")
        self.selectVideo_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectVideo_button.setGeometry(QtCore.QRect(170, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectVideo_button.setFont(font)
        self.selectVideo_button.setObjectName("selectVideo_button")
        self.selectVideo_text = QtWidgets.QLineEdit(self.centralwidget)
        self.selectVideo_text.setGeometry(QtCore.QRect(280, 180, 321, 31))
        self.selectVideo_text.setObjectName("selectVideo_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my definitions
        self.face_scanner = FaceScanner()

        # connect buttons
        self.selectDir_button.clicked.connect(self.selectDir)
        self.selectNewDir_button.clicked.connect(self.selectWorkingDir)
        self.train_button.clicked.connect(self.train)
        self.findPeople_button.clicked.connect(self.find)
        self.addNewPerson_button.clicked.connect(self.addNew)
        self.selectVideo_button.clicked.connect(self.selectVideo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.selectDir_button.setText(_translate("MainWindow", "Select Directory"))
        self.label_2.setText(_translate("MainWindow", "OR"))
        self.label_3.setText(_translate("MainWindow", "People"))
        self.addNewPerson_button.setText(_translate("MainWindow", "Add New Person"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.train_button.setText(_translate("MainWindow", "Train"))
        self.label_5.setText(_translate("MainWindow", "Working Path"))
        self.selectNewDir_button.setText(_translate("MainWindow", "Select New Directory"))
        self.label_6.setText(_translate("MainWindow", "Your model and processed images are saved here."))
        self.findPeople_button.setText(_translate("MainWindow", "Find People"))
        self.selectVideo_button.setText(_translate("MainWindow", "Select Video"))

    def selectDir(self):
        file = str(QFileDialog.getExistingDirectory(caption="Select Directory"))
        self.path_box.setText(file)

    def selectWorkingDir(self):
        file = str(QFileDialog.getExistingDirectory(caption="Select Directory"))
        self.workingPath_box.setText(file)

    def preprocess(self):
        path = self.path_box.text()
        to_directory = self.workingPath_box.text()
        self.face_scanner.preprocess_images(path, to_directory)


    def msgBox(self, title, message):
        QMessageBox.about(None, title, message)

    def split_data(self):
        to_directory = self.workingPath_box.text()
        path = to_directory + "/" + getDirectoryName(self.path_box.text())
        to_dir = to_directory + "/" + "SplitData"
        self.face_scanner.split_test_train(path, to_dir)


    def train(self):
        if self.path_box.text() and self.workingPath_box.text():
            self.msgBox("Info!", "Started preporcessing")
            self.preprocess()
            self.msgBox("Info!", "Started splitting data")
            self.split_data()
            self.msgBox("Info!", "Your data set training...")
            to_directory = self.workingPath_box.text()
            to_dir = to_directory + "/" + "SplitData"
            dataset = DataSet(to_dir, (64, 64))
            dataset.createNeuralNetwork()
            dataset.process_images()
            dataset.save_model()
            self.msgBox("Info!", "Process finished")
        else:
            self.msgBox("Warning", "Please enter path and working path")

    def find(self):
        if self.workingPath_box.text():
            model_name = self.workingPath_box.text() + "/" + "SplitData" + "/" + "SplitData"
            self.face_scanner.objects = self.face_scanner.getObjects(self.workingPath_box.text() + "/SplitData/test_set")
            print(self.face_scanner.objects)
            self.person_list.clear()

            if self.selectVideo_text.text():
                objects = self.face_scanner.recognize_face(model_name, path=self.selectVideo_text.text())
            else:
                objects = self.face_scanner.recognize_face(model_name)

            for i in objects:
                QListWidgetItem(i, self.person_list)

        else:
            self.msgBox("Warning", "Please enter working path")

    def addNew(self):
        if self.path_box.text():
            person_name = self.personName_box.text()
            path = self.path_box.text()
            self.face_scanner.scan_person(person_name, path)
        else:
            self.msgBox("Warning", "Please enter path")

    def selectVideo(self):
        file = str(QFileDialog.getOpenFileName(caption="Select Video", filter="Video files (*.mp4 *.avi)")[0])
        self.selectVideo_text.setText(file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
