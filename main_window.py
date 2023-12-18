import sys
import datetime
import os
import csv
import string

import week
import year
import script
import split_date_data
import Iterator

from os import path
from datetime import *

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Window")
        MainWindow.setFixedSize(461, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_file = QtWidgets.QPushButton(self.centralwidget)
        self.main_file.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.main_file.setObjectName("pushButton")
        self.main_file.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_datae = QtWidgets.QPushButton(self.centralwidget)
        self.cut_datae.setGeometry(QtCore.QRect(170, 10, 121, 51))
        self.cut_datae.setObjectName("pushButton_2")
        self.cut_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_datae = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_datae.setGeometry(QtCore.QRect(230, 71, 60, 20))
        self.folder_for_datae.setObjectName("select_pushButton_2")
        self.folder_for_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_years = QtWidgets.QPushButton(self.centralwidget)
        self.cut_years.setGeometry(QtCore.QRect(330, 10, 121, 51))
        self.cut_years.setObjectName("pushButton_3")
        self.cut_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_years = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_years.setGeometry(QtCore.QRect(390, 71, 60, 20))
        self.folder_for_years.setObjectName("select_pushButton_3")
        self.folder_for_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.cut_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.cut_weaks.setGeometry(QtCore.QRect(330, 100, 121, 51))
        self.cut_weaks.setObjectName("pushButton_4")
        self.cut_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.folder_for_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.folder_for_weaks.setGeometry(QtCore.QRect(390, 160, 60, 20))
        self.folder_for_weaks.setObjectName("select_pushButton_4")
        self.folder_for_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 121, 51))
        self.textEdit.setObjectName("textEdit")

        self.find_years = QtWidgets.QPushButton(self.centralwidget)
        self.find_years.setGeometry(QtCore.QRect(50, 180, 81, 21))
        self.find_years.setObjectName("pushButton_5")
        self.find_years.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)
        self.find_weaks = QtWidgets.QPushButton(self.centralwidget)
        self.find_weaks.setGeometry(QtCore.QRect(50, 205, 81, 21))
        self.find_weaks.setObjectName("pushButton_6")
        self.find_weaks.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)
        self.find_datae = QtWidgets.QPushButton(self.centralwidget)
        self.find_datae.setGeometry(QtCore.QRect(50, 155, 81, 21))
        self.find_datae.setObjectName("pushButton_7")
        self.find_datae.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:blue;
            color:white;
            border: 1px solid black;
        }
    """)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(133, 90, 190, 100))
        self.label.setObjectName("label")
        self.label.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_file.setText(_translate("MainWindow", "Select main file"))

        self.folder_for_datae.setText(
            _translate("MainWindow", "add folder"))
        self.cut_datae.setText(_translate("MainWindow", "Split by data/date"))

        self.folder_for_years.setText(
            _translate("MainWindow", "add folder"))
        self.cut_years.setText(_translate("MainWindow", "Split by years"))

        self.cut_weaks.setText(_translate("MainWindow", "Split by weaks"))
        self.folder_for_weaks.setText(
            _translate("MainWindow", "add folder"))

        self.find_years.setText(_translate("MainWindow", "find in years"))
        self.find_weaks.setText(_translate("MainWindow", "find in weeks"))
        self.find_datae.setText(_translate("MainWindow", "find in data/e"))
        self.label.setText(_translate("MainWindow", ""))


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_file.clicked.connect(self.select_main_filepath)
        self.ui.folder_for_datae.clicked.connect(
            self.select_folder_for_datae)
        self.ui.folder_for_years.clicked.connect(
            self.select_folder_for_years)
        self.ui.folder_for_weaks.clicked.connect(
            self.select_folder_for_weaks)
        self.ui.find_years.clicked.connect(self.get_data_years)
        self.ui.find_weaks.clicked.connect(self.get_data_weaks)
        self.ui.find_datae.clicked.connect(self.get_data_datae)
        self.ui.cut_datae.clicked.connect(self.cut_by_datae)
        self.ui.cut_years.clicked.connect(self.cut_by_years)
        self.ui.cut_weaks.clicked.connect(self.cut_by_weaks)

    def select_main_filepath(self) -> None:
        """select path for original dataset
        """
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')[
            0]
        if ".csv" == path.splitext(filepath)[1]:
            self.main_path = filepath
            self.iter = Iterator.Iterator(filepath)
            self.ui.label.setText("")
            QMessageBox.about(self, "Selection", "dataset selected")
        else:
            self.ui.label.setText("Chosen file needs to be .csv")

    def select_folder_for_datae(self) -> None:
        """select filepath for data/date cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.datae_path = folderpath
        QMessageBox.about(self, "Selection", "Folder selected")

    def select_folder_for_years(self) -> None:
        """select filepath for years cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.years_path = folderpath
        QMessageBox.about(self, "Selection", "Folder selected")

    def select_folder_for_weaks(self) -> None:
        """select filepath for weaks cut
        """
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        self.weaks_path = folderpath
        QMessageBox.about(self, "Selection", "Folder selected")

    def get_data_years(self) -> None:
        """find date in dataset with years
        """
        try:
            cur_data = datetime.strptime(self.ui.textEdit.text(), "%Y-%m-%d")
            data = str(script.find_3(self.years_path, cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def get_data_weaks(self) -> None:
        """find date in dataset with weaks
        """
        try:
            cur_data = datetime.strptime(self.ui.textEdit.text(), "%Y-%m-%d")

            data = str(script.find_4(self.weaks_path, cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def get_data_datae(self) -> None:
        """find date in dataset with data/date
        """
        try:
            print(self.datae_path)
            cur_data = datetime.strptime(self.ui.textEdit.text(), "%Y-%m-%d")

            data = str(script.find_2(os.path.join(self.datae_path,
                                                  "X.csv"), os.path.join(self.datae_path, "Y.csv"), cur_data))
            self.ui.label.setText(data)
        except:
            self.ui.label.setText("no file path")

    def cut_by_datae(self) -> None:
        """cut original dataset on data/date
        """
        try:
            split_date_data.file_cut_date_and_data(
                self.main_path, self.datae_path)
        except:
            self.ui.label.setText("no file path")

    def cut_by_years(self) -> None:
        """cut original dataset on years
        """
        try:
            year.N_cut_by_year(self.main_path, self.years_path)
        except:
            self.ui.label.setText("no file path")

    def cut_by_weaks(self) -> None:
        """cut original dataset on weaks
        """
        try:
            week.N_cut_by_week(self.main_path, self.weaks_path)
        except:
            self.ui.label.setText("no file path")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
