# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/dialog_createProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_createProject(object):
    def setupUi(self, Dialog_createProject):
        Dialog_createProject.setObjectName("Dialog_createProject")
        Dialog_createProject.resize(368, 227)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_createProject)
        self.buttonBox.setGeometry(QtCore.QRect(190, 180, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_createProject)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setObjectName("label")
        self.textEdit_name = QtWidgets.QTextEdit(Dialog_createProject)
        self.textEdit_name.setGeometry(QtCore.QRect(70, 17, 281, 21))
        self.textEdit_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setObjectName("textEdit_name")
        self.label_2 = QtWidgets.QLabel(Dialog_createProject)
        self.label_2.setGeometry(QtCore.QRect(20, 123, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox_field = QtWidgets.QComboBox(Dialog_createProject)
        self.comboBox_field.setGeometry(QtCore.QRect(70, 120, 191, 22))
        self.comboBox_field.setObjectName("comboBox_field")
        self.pushButton_newField = QtWidgets.QPushButton(Dialog_createProject)
        self.pushButton_newField.setGeometry(QtCore.QRect(280, 120, 75, 25))
        self.pushButton_newField.setObjectName("pushButton_newField")
        self.textEdit_goal = QtWidgets.QTextEdit(Dialog_createProject)
        self.textEdit_goal.setGeometry(QtCore.QRect(70, 47, 281, 61))
        self.textEdit_goal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setObjectName("textEdit_goal")
        self.label_3 = QtWidgets.QLabel(Dialog_createProject)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog_createProject)
        self.buttonBox.accepted.connect(Dialog_createProject.accept)
        self.buttonBox.rejected.connect(Dialog_createProject.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_createProject)

    def retranslateUi(self, Dialog_createProject):
        _translate = QtCore.QCoreApplication.translate
        Dialog_createProject.setWindowTitle(_translate("Dialog_createProject", "Create New Project"))
        self.label.setText(_translate("Dialog_createProject", "Name:"))
        self.label_2.setText(_translate("Dialog_createProject", "Field:"))
        self.pushButton_newField.setText(_translate("Dialog_createProject", "New Field"))
        self.label_3.setText(_translate("Dialog_createProject", "Goal:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_createProject = QtWidgets.QDialog()
    ui = Ui_Dialog_createProject()
    ui.setupUi(Dialog_createProject)
    Dialog_createProject.show()
    sys.exit(app.exec_())
