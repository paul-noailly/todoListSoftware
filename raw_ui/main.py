# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1618, 989)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 1121, 251))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_project = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_project.setGeometry(QtCore.QRect(10, 90, 1091, 141))
        self.tableWidget_project.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_project.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_project.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_project.setAutoScroll(True)
        self.tableWidget_project.setDragEnabled(False)
        self.tableWidget_project.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_project.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_project.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_project.setObjectName("tableWidget_project")
        self.tableWidget_project.setColumnCount(8)
        self.tableWidget_project.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_project.setHorizontalHeaderItem(7, item)
        self.tableWidget_project.horizontalHeader().setVisible(True)
        self.tableWidget_project.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_project.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_project.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_project.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_project.horizontalHeader().setStretchLastSection(False)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 341, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label.setObjectName("label")
        self.comboBox_projectFilterField = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_projectFilterField.setGeometry(QtCore.QRect(60, 17, 141, 22))
        self.comboBox_projectFilterField.setObjectName("comboBox_projectFilterField")
        self.checkBox_projectShowComplete = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_projectShowComplete.setGeometry(QtCore.QRect(220, 20, 111, 17))
        self.checkBox_projectShowComplete.setTristate(True)
        self.checkBox_projectShowComplete.setObjectName("checkBox_projectShowComplete")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(370, 20, 161, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_projectSort = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_projectSort.setGeometry(QtCore.QRect(30, 17, 121, 22))
        self.comboBox_projectSort.setObjectName("comboBox_projectSort")
        self.comboBox_projectSort.addItem("")
        self.comboBox_projectSort.addItem("")
        self.comboBox_projectSort.addItem("")
        self.comboBox_projectSort.addItem("")
        self.comboBox_projectSort.addItem("")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(560, 20, 161, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_projectCreate = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_projectCreate.setGeometry(QtCore.QRect(10, 17, 141, 25))
        self.pushButton_projectCreate.setObjectName("pushButton_projectCreate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 290, 1121, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 30, 371, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_subProjectFilterField = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_subProjectFilterField.setGeometry(QtCore.QRect(80, 17, 141, 22))
        self.comboBox_subProjectFilterField.setObjectName("comboBox_subProjectFilterField")
        self.checkBox_subProjectShowCompleted = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_subProjectShowCompleted.setGeometry(QtCore.QRect(240, 20, 111, 17))
        self.checkBox_subProjectShowCompleted.setObjectName("checkBox_subProjectShowCompleted")
        self.tableWidget_subProject = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_subProject.setGeometry(QtCore.QRect(20, 100, 1081, 151))
        self.tableWidget_subProject.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_subProject.setAutoScroll(True)
        self.tableWidget_subProject.setDragEnabled(False)
        self.tableWidget_subProject.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_subProject.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_subProject.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_subProject.setObjectName("tableWidget_subProject")
        self.tableWidget_subProject.setColumnCount(8)
        self.tableWidget_subProject.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_subProject.setHorizontalHeaderItem(7, item)
        self.tableWidget_subProject.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_subProject.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_subProject.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_subProject.verticalHeader().setSortIndicatorShown(True)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(400, 30, 161, 51))
        self.groupBox_7.setObjectName("groupBox_7")
        self.comboBox_subProjectSort = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_subProjectSort.setGeometry(QtCore.QRect(20, 20, 121, 22))
        self.comboBox_subProjectSort.setObjectName("comboBox_subProjectSort")
        self.comboBox_subProjectSort.addItem("")
        self.comboBox_subProjectSort.addItem("")
        self.comboBox_subProjectSort.addItem("")
        self.comboBox_subProjectSort.addItem("")
        self.comboBox_subProjectSort.addItem("")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_9.setGeometry(QtCore.QRect(580, 30, 161, 51))
        self.groupBox_9.setObjectName("groupBox_9")
        self.pushButton_subProjectCreate = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_subProjectCreate.setGeometry(QtCore.QRect(10, 17, 141, 25))
        self.pushButton_subProjectCreate.setObjectName("pushButton_subProjectCreate")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 570, 1121, 391))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_10.setGeometry(QtCore.QRect(200, 30, 161, 51))
        self.groupBox_10.setObjectName("groupBox_10")
        self.comboBox_taskSort = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_taskSort.setGeometry(QtCore.QRect(30, 20, 121, 22))
        self.comboBox_taskSort.setObjectName("comboBox_taskSort")
        self.comboBox_taskSort.addItem("")
        self.comboBox_taskSort.addItem("")
        self.tableWidget_task = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_task.setGeometry(QtCore.QRect(20, 100, 1081, 281))
        self.tableWidget_task.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_task.setAutoScroll(True)
        self.tableWidget_task.setDragEnabled(False)
        self.tableWidget_task.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_task.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_task.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_task.setObjectName("tableWidget_task")
        self.tableWidget_task.setColumnCount(5)
        self.tableWidget_task.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_task.setHorizontalHeaderItem(4, item)
        self.tableWidget_task.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_task.horizontalHeader().setMinimumSectionSize(30)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_11.setGeometry(QtCore.QRect(380, 30, 161, 51))
        self.groupBox_11.setObjectName("groupBox_11")
        self.pushButton_taskCreate = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_taskCreate.setGeometry(QtCore.QRect(10, 17, 141, 25))
        self.pushButton_taskCreate.setObjectName("pushButton_taskCreate")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 30, 161, 51))
        self.groupBox_12.setObjectName("groupBox_12")
        self.checkBox_TaskFilterShowCompleted = QtWidgets.QCheckBox(self.groupBox_12)
        self.checkBox_TaskFilterShowCompleted.setGeometry(QtCore.QRect(40, 20, 111, 17))
        self.checkBox_TaskFilterShowCompleted.setObjectName("checkBox_TaskFilterShowCompleted")
        self.groupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_13.setGeometry(QtCore.QRect(1160, 20, 431, 941))
        self.groupBox_13.setObjectName("groupBox_13")
        self.widget_graphTemporel = QtWidgets.QWidget(self.groupBox_13)
        self.widget_graphTemporel.setGeometry(QtCore.QRect(20, 110, 391, 281))
        self.widget_graphTemporel.setObjectName("widget_graphTemporel")
        self.comboBox_statsTopictoPlot = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_statsTopictoPlot.setGeometry(QtCore.QRect(20, 70, 141, 22))
        self.comboBox_statsTopictoPlot.setObjectName("comboBox_statsTopictoPlot")
        self.comboBox_statsTopictoPlot.addItem("")
        self.comboBox_statsTopictoPlot.addItem("")
        self.comboBox_statsTopictoPlot.addItem("")
        self.comboBox_statsTopictoPlot.addItem("")
        self.comboBox_statsFrequencyToPlot = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_statsFrequencyToPlot.setGeometry(QtCore.QRect(170, 70, 61, 22))
        self.comboBox_statsFrequencyToPlot.setObjectName("comboBox_statsFrequencyToPlot")
        self.comboBox_statsFrequencyToPlot.addItem("")
        self.comboBox_statsFrequencyToPlot.addItem("")
        self.checkBox_statsCumulativetoPlot = QtWidgets.QCheckBox(self.groupBox_13)
        self.checkBox_statsCumulativetoPlot.setGeometry(QtCore.QRect(240, 74, 81, 17))
        self.checkBox_statsCumulativetoPlot.setObjectName("checkBox_statsCumulativetoPlot")
        self.comboBox_statsProjectToPlot = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_statsProjectToPlot.setGeometry(QtCore.QRect(100, 37, 61, 22))
        self.comboBox_statsProjectToPlot.setObjectName("comboBox_statsProjectToPlot")
        self.comboBox_statsProjectToPlot.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_13)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_5.setObjectName("label_5")
        self.textBrowser_nameProject2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_nameProject2.setGeometry(QtCore.QRect(118, 566, 131, 21))
        self.textBrowser_nameProject2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameProject2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameProject2.setObjectName("textBrowser_nameProject2")
        self.textBrowser_nameSubProject = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_nameSubProject.setGeometry(QtCore.QRect(340, 566, 151, 21))
        self.textBrowser_nameSubProject.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameSubProject.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameSubProject.setObjectName("textBrowser_nameSubProject")
        self.textBrowser_nameProject = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_nameProject.setGeometry(QtCore.QRect(150, 286, 151, 21))
        self.textBrowser_nameProject.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameProject.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_nameProject.setObjectName("textBrowser_nameProject")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Project"))
        item = self.tableWidget_project.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Done"))
        item = self.tableWidget_project.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project"))
        item = self.tableWidget_project.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Field"))
        item = self.tableWidget_project.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Content"))
        item = self.tableWidget_project.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.tableWidget_project.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Update Date"))
        item = self.tableWidget_project.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "% Done"))
        item = self.tableWidget_project.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Delete"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Filters"))
        self.label.setText(_translate("MainWindow", "Field:"))
        self.checkBox_projectShowComplete.setText(_translate("MainWindow", "Show Completed"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sort"))
        self.comboBox_projectSort.setItemText(0, _translate("MainWindow", "Project"))
        self.comboBox_projectSort.setItemText(1, _translate("MainWindow", "Field"))
        self.comboBox_projectSort.setItemText(2, _translate("MainWindow", "Start Date"))
        self.comboBox_projectSort.setItemText(3, _translate("MainWindow", "Update Date"))
        self.comboBox_projectSort.setItemText(4, _translate("MainWindow", "% Done"))
        self.groupBox_8.setTitle(_translate("MainWindow", "New"))
        self.pushButton_projectCreate.setText(_translate("MainWindow", "Create New Project"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sub Project of project:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Filters"))
        self.label_3.setText(_translate("MainWindow", "Sub Field:"))
        self.checkBox_subProjectShowCompleted.setText(_translate("MainWindow", "Show Completed"))
        item = self.tableWidget_subProject.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Done"))
        item = self.tableWidget_subProject.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sub Project"))
        item = self.tableWidget_subProject.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sub Field"))
        item = self.tableWidget_subProject.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Content"))
        item = self.tableWidget_subProject.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.tableWidget_subProject.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Update Date"))
        item = self.tableWidget_subProject.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "% Done"))
        item = self.tableWidget_subProject.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Delete"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Sort"))
        self.comboBox_subProjectSort.setItemText(0, _translate("MainWindow", "Sub Project"))
        self.comboBox_subProjectSort.setItemText(1, _translate("MainWindow", "Sub Field"))
        self.comboBox_subProjectSort.setItemText(2, _translate("MainWindow", "Start Date"))
        self.comboBox_subProjectSort.setItemText(3, _translate("MainWindow", "Update Date"))
        self.comboBox_subProjectSort.setItemText(4, _translate("MainWindow", "% Done"))
        self.groupBox_9.setTitle(_translate("MainWindow", "New"))
        self.pushButton_subProjectCreate.setText(_translate("MainWindow", "Create Sub Project"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Task For Project:                                                 An Sub Project: "))
        self.groupBox_10.setTitle(_translate("MainWindow", "Sort"))
        self.comboBox_taskSort.setItemText(0, _translate("MainWindow", "Task"))
        self.comboBox_taskSort.setItemText(1, _translate("MainWindow", "Start Date"))
        item = self.tableWidget_task.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Done"))
        item = self.tableWidget_task.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task"))
        item = self.tableWidget_task.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Content"))
        item = self.tableWidget_task.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.tableWidget_task.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Delete"))
        self.groupBox_11.setTitle(_translate("MainWindow", "New"))
        self.pushButton_taskCreate.setText(_translate("MainWindow", "Create Task"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Filters"))
        self.checkBox_TaskFilterShowCompleted.setText(_translate("MainWindow", "Show Completed"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Statistics"))
        self.comboBox_statsTopictoPlot.setItemText(0, _translate("MainWindow", "Completed Tasks"))
        self.comboBox_statsTopictoPlot.setItemText(1, _translate("MainWindow", "Created Task"))
        self.comboBox_statsTopictoPlot.setItemText(2, _translate("MainWindow", "Created Sub Project"))
        self.comboBox_statsTopictoPlot.setItemText(3, _translate("MainWindow", "Completed Sub Project"))
        self.comboBox_statsFrequencyToPlot.setItemText(0, _translate("MainWindow", "Weekly"))
        self.comboBox_statsFrequencyToPlot.setItemText(1, _translate("MainWindow", "Daily"))
        self.checkBox_statsCumulativetoPlot.setText(_translate("MainWindow", "Cumulative"))
        self.comboBox_statsProjectToPlot.setItemText(0, _translate("MainWindow", "All"))
        self.label_5.setText(_translate("MainWindow", "Project to plot:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())