# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageBoxExample(object):
    def setupUi(self, MessageBoxExample):
        MessageBoxExample.setObjectName("MessageBoxExample")
        MessageBoxExample.resize(423, 280)
        self.centralwidget = QtWidgets.QWidget(MessageBoxExample)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 141, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        MessageBoxExample.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MessageBoxExample)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 26))
        self.menubar.setObjectName("menubar")
        MessageBoxExample.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MessageBoxExample)
        self.statusbar.setObjectName("statusbar")
        MessageBoxExample.setStatusBar(self.statusbar)

        self.retranslateUi(MessageBoxExample)
        QtCore.QMetaObject.connectSlotsByName(MessageBoxExample)

    def retranslateUi(self, MessageBoxExample):
        _translate = QtCore.QCoreApplication.translate
        MessageBoxExample.setWindowTitle(_translate("MessageBoxExample", "Message Box Example"))
        self.pushButton.setText(_translate("MessageBoxExample", "Click Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageBoxExample = QtWidgets.QMainWindow()
    ui = Ui_MessageBoxExample()
    ui.setupUi(MessageBoxExample)
    MessageBoxExample.show()
    sys.exit(app.exec_())

