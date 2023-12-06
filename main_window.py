import sys
import datetime
import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap

import week
import year
import script
import split_date_data

class Window2(QWidget):
    def __init__(self, date: datetime.date) -> None:
        super().__init__()

        self.setGeometry(500, 500, 500, 500)
        self.background_2 = QLabel(self)
        self.fire = QLabel(self)
        self.setWindowTitle('Выбор файла')

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Light))
        self.base.setText("Найти данные в файле по дате")
        self.base.move(100, 10)
        self.base.setStyleSheet("background-color: white; border: 1px solid black;")
        self.base.adjustSize()        

        self.b2_4 = QPushButton('dataset', self)
        self.b2_4.resize(300, 160)
        self.b2_4.move(105, 180)
        self.b2_4.clicked.connect(lambda: self.findbydataset(date))

    def findbydataset(self, date: datetime.date) -> None:
        tmp = script.find_1("dataset.csv",date)
        if tmp == None:            
            QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : Не найдены")
        else:
            QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp[1]}")


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        
        super(Window, self).__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Value by Dates")
        self.background = QLabel(self)
        self.fire = QLabel(self)

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.base.setText("Создание и выбор аннотаций")
        self.base.move(130, 10)
        self.base.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')[0]

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Разделение на года")
        self.b1.setFixedSize(200, 50)
        self.b1.move(200, 100)
        self.b1.clicked.connect(self.sort_year)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Разделение на недели")
        self.b2.setFixedSize(200, 50)
        self.b2.move(200, 150)
        self.b2.clicked.connect(self.sort_week)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Разделение на даты и данные")
        self.b3.setFixedSize(200, 50)
        self.b3.move(200, 200)
        self.b3.clicked.connect(self.sort_data_date)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ввести дату")
        self.b4.setFixedSize(200, 50)
        self.b4.move(200, 300)
        self.b4.clicked.connect(self.input_data)
    
    def sort_data_date(self) -> None:
        split_date_data.file_cut_date_and_data(self.folderpath_dataset)
        QMessageBox.about(self, "Sort", "Sorting by date")
        
    def sort_week(self) -> None:
        week.N_cut_by_week("dataset.csv")
        QMessageBox.about(self, "Sort", "Sorting by week")

    def sort_year(self) -> None:
        year.N_cut_by_year("dataset.csv")
        QMessageBox.about(self, "Sort", "Sorting by year")
        
        
    def check_date(self, text: str) -> bool:
        Flag = False        
        if (0 <= int(text[8:10]) <= 31 and 0 <= int(text[5:7]) <= 12 and 2008 <= int(text[0:4]) <= 2023): return True
        else: return False

    def input_data(self) -> None:
        """a function that accepts a date and checks it for correctness"""
        text, ok = QInputDialog.getText(self, 'Data', 'Enter the data in the format yyyy-mm-dd:')
        dictionary = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ok:
            if self.check_date(text) == True:
                        if  int(text[8:10])<=dictionary[int(text[5:7])]:
                            u=text[0:4]
                            m=text[5:7]
                            d=text[8:10]
                            date = datetime.date(int(text[0:4]), int(text[5:7]), int(text[8:10]))
                            self.show_window_2(date)
                        else:  QMessageBox.about(self, "warning!\n", "Неправильные данные...")
            else:  QMessageBox.about(self, "warning!\n", "Неправильный формат входных данных...")

    def show_window_2(self, date: datetime.date) -> None:
        self.w2 = Window2(date)
        self.w2.show()


def application() -> None:
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    
    application()