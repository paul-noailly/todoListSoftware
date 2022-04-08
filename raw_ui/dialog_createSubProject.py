# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/dialog_createSubProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_createSubProject(object):
    def setupUi(self, Dialog_createSubProject):
        Dialog_createSubProject.setObjectName("Dialog_createSubProject")
        Dialog_createSubProject.resize(374, 204)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_createSubProject)
        self.buttonBox.setGeometry(QtCore.QRect(190, 160, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Dialog_createSubProject)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.textEdit_name = QtWidgets.QTextEdit(Dialog_createSubProject)
        self.textEdit_name.setGeometry(QtCore.QRect(70, 20, 281, 21))
        self.textEdit_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_name.setObjectName("textEdit_name")
        self.textEdit_goal = QtWidgets.QTextEdit(Dialog_createSubProject)
        self.textEdit_goal.setGeometry(QtCore.QRect(70, 47, 281, 61))
        self.textEdit_goal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_goal.setObjectName("textEdit_goal")
        self.label = QtWidgets.QLabel(Dialog_createSubProject)
        self.label.setGeometry(QtCore.QRect(20, 23, 47, 13))
        self.label.setObjectName("label")
        self.comboBox_field = QtWidgets.QComboBox(Dialog_createSubProject)
        self.comboBox_field.setGeometry(QtCore.QRect(70, 120, 191, 22))
        self.comboBox_field.setObjectName("comboBox_field")
        self.label_2 = QtWidgets.QLabel(Dialog_createSubProject)
        self.label_2.setGeometry(QtCore.QRect(20, 123, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton_newField = QtWidgets.QPushButton(Dialog_createSubProject)
        self.pushButton_newField.setGeometry(QtCore.QRect(274, 120, 81, 25))
        self.pushButton_newField.setObjectName("pushButton_newField")

        self.retranslateUi(Dialog_createSubProject)
        self.buttonBox.accepted.connect(Dialog_createSubProject.accept)
        self.buttonBox.rejected.connect(Dialog_createSubProject.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_createSubProject)

    def retranslateUi(self, Dialog_createSubProject):
        _translate = QtCore.QCoreApplication.translate
        Dialog_createSubProject.setWindowTitle(_translate("Dialog_createSubProject", "Create New Sub Project"))
        self.label_3.setText(_translate("Dialog_createSubProject", "Goal:"))
        self.label.setText(_translate("Dialog_createSubProject", "Name:"))
        self.label_2.setText(_translate("Dialog_createSubProject", "Field:"))
        self.pushButton_newField.setText(_translate("Dialog_createSubProject", "New Sub Field"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_createSubProject = QtWidgets.QDialog()
    ui = Ui_Dialog_createSubProject()
    ui.setupUi(Dialog_createSubProject)
    Dialog_createSubProject.show()
    sys.exit(app.exec_())
