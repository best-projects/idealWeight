# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ideal_weight_calculate import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Height = QtWidgets.QLineEdit(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(90, 90, 101, 41))
        self.Height.setObjectName("Height")
        self.Weight = QtWidgets.QLineEdit(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(90, 140, 101, 41))
        self.Weight.setObjectName("Weight")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 81, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 81, 41))
        self.label_2.setObjectName("label_2")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(100, 250, 81, 41))
        self.Calculate.setObjectName("Calculate")
        self.select = QtWidgets.QComboBox(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(90, 190, 101, 41))
        self.select.setEditable(False)
        self.select.setObjectName("select")
        self.select.addItem("")
        self.select.addItem("")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(195, 90, 271, 201))
        self.log.setObjectName("log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Calculate.clicked.connect(self.calculate_ideal_weight)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "height(cm)"))
        self.label_2.setText(_translate("MainWindow", "weight(kg)"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.select.setItemText(0, _translate("MainWindow", "Female"))
        self.select.setItemText(1, _translate("MainWindow", "Male"))

    def calculate_ideal_weight(self):
        self.log.clear()
        weight_input = int(self.Weight.text())
        height_input = int(self.Height.text())
        cal_bmi = bmi(weight_input, height_input / 100)
        gender = self.select.currentIndex()
        cal_ibw = round(ibw(height_input, gender))
        self.log.append(cal_bmi)
        self.log.append("\nIdeal_weight  : %s   "%str(cal_ibw))
        # self.result.setText(str(cal_bmi))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
