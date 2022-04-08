# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/dialog_createTask.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np, pandas as pd, datetime, time, json, os


class Ui_Dialog_createTask(object):
    def setupUi(self, Dialog_createTask):
        Dialog_createTask.setObjectName("Dialog_createTask")
        Dialog_createTask.resize(386, 190)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_createTask)
        self.buttonBox.setGeometry(QtCore.QRect(200, 140, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Dialog_createTask)
        self.label_3.setGeometry(QtCore.QRect(30, 63, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog_createTask)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.textEdit_name = QtWidgets.QTextEdit(Dialog_createTask)
        self.textEdit_name.setGeometry(QtCore.QRect(80, 27, 281, 21))
        self.textEdit_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setObjectName("textEdit_name")
        self.textEdit_name.setTabChangesFocus(True)
        self.textEdit_goal = QtWidgets.QTextEdit(Dialog_createTask)
        self.textEdit_goal.setGeometry(QtCore.QRect(80, 60, 281, 61))
        self.textEdit_goal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setObjectName("textEdit_goal")
        self.textEdit_goal.setTabChangesFocus(True)

        self.retranslateUi(Dialog_createTask)
        self.buttonBox.accepted.connect(Dialog_createTask.accept)
        self.buttonBox.rejected.connect(Dialog_createTask.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_createTask)

    def retranslateUi(self, Dialog_createTask):
        self._translate = QtCore.QCoreApplication.translate
        Dialog_createTask.setWindowTitle(self._translate("Dialog_createTask", "Create New Task"))
        self.label_3.setText(self._translate("Dialog_createTask", "Goal:"))
        self.label.setText(self._translate("Dialog_createTask", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_createTask = QtWidgets.QDialog()
    ui = Ui_Dialog_createTask()
    ui.setupUi(Dialog_createTask)
    Dialog_createTask.show()
    sys.exit(app.exec_())
