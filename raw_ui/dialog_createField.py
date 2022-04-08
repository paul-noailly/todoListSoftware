# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/dialog_createField.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_createField(object):
    def setupUi(self, Dialog_createField):
        Dialog_createField.setObjectName("Dialog_createField")
        Dialog_createField.resize(296, 107)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_createField)
        self.buttonBox.setGeometry(QtCore.QRect(100, 60, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog_createField)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 241, 21))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog_createField)
        self.buttonBox.accepted.connect(Dialog_createField.accept)
        self.buttonBox.rejected.connect(Dialog_createField.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_createField)

    def retranslateUi(self, Dialog_createField):
        _translate = QtCore.QCoreApplication.translate
        Dialog_createField.setWindowTitle(_translate("Dialog_createField", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_createField = QtWidgets.QDialog()
    ui = Ui_Dialog_createField()
    ui.setupUi(Dialog_createField)
    Dialog_createField.show()
    sys.exit(app.exec_())
