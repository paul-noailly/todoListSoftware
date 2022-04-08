# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/dialog_createSubField.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_createSubField(object):
    def setupUi(self, Dialog_createSubField):
        Dialog_createSubField.setObjectName("Dialog_createSubField")
        Dialog_createSubField.resize(294, 107)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_createSubField)
        self.buttonBox.setGeometry(QtCore.QRect(100, 60, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog_createSubField)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 241, 21))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog_createSubField)
        self.buttonBox.accepted.connect(Dialog_createSubField.accept)
        self.buttonBox.rejected.connect(Dialog_createSubField.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_createSubField)

    def retranslateUi(self, Dialog_createSubField):
        _translate = QtCore.QCoreApplication.translate
        Dialog_createSubField.setWindowTitle(_translate("Dialog_createSubField", "Create New Sub Field"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_createSubField = QtWidgets.QDialog()
    ui = Ui_Dialog_createSubField()
    ui.setupUi(Dialog_createSubField)
    Dialog_createSubField.show()
    sys.exit(app.exec_())
