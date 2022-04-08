# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np, pandas as pd, datetime, time, json, os, matplotlib
# create project
from classes.dialog_createProject import Ui_Dialog_createProject
from classes.dialog_createField import Ui_Dialog_createField
# create sub projecte
from classes.dialog_createSubProject import Ui_Dialog_createSubProject
from classes.dialog_createSubField import Ui_Dialog_createSubField
# create task
from classes.dialog_createTask import Ui_Dialog_createTask
# graph
from classes.graph_temporel import MplCanvas
import pyqtgraph as pg
from pyqtgraph.Point import Point

class DataExtractor():
    def __init__(self):
        pass

    def get_list_project(self):        
        list_project = []
        for filename in os.listdir('data'):
            with open('data/'+filename,'r') as f:
                dic = json.load(f)
                list_project.append(dic)
                f.close()
        return list_project

    def get_data_task(self):
        list_project = self.get_list_project()
        list_data = []
        for project in list_project:
            for sub_project_name,sub_project  in project['sub_projects'].items():
                for task_name, task in sub_project['tasks'].items():
                    if task['completed']:
                        list_data.append({'project':project['name'],'sub_project':sub_project_name,'task':task_name,'start_time':task['start_time'],'end_time':task['completed_time'],'completed':1})
                    else:
                        list_data.append({'project':project['name'],'sub_project':sub_project_name,'task':task_name,'start_time':task['start_time'],'end_time':task['completed_time'],'completed':0})
        df = pd.DataFrame(list_data)
        df.loc[:,'start_date'] = pd.to_datetime(df.start_time, unit='s')
        df.loc[:,'end_date'] = pd.to_datetime(df.end_time, unit='s')
        return df

    def get_data_subProject(self):
        list_project = self.get_list_project()
        list_data = []
        for project in list_project:
            for sub_project_name,sub_project  in project['sub_projects'].items():
                if sub_project['completed']:
                    list_data.append({'project':project['name'],'sub_project':sub_project_name,'start_time':sub_project['start_time'],'end_time':sub_project['completed_time'],'completed':1})
                else:
                    list_data.append({'project':project['name'],'sub_project':sub_project_name,'start_time':sub_project['start_time'],'end_time':sub_project['completed_time'],'completed':0})
        df = pd.DataFrame(list_data)
        df.loc[:,'start_date'] = pd.to_datetime(df.start_time, unit='s')
        df.loc[:,'end_date'] = pd.to_datetime(df.end_time, unit='s')
        return df

    def get_arrays(self, filter_project, topic, freq):
        if topic == 'Completed Tasks':
            df = self.get_data_task()
            if filter_project != 'All':
                df = df.loc[df.project==filter_project]
            if freq == 'Daily':
                df = df.set_index(df.end_date).resample('1d').sum().reset_index()
            else:
                df = df.set_index(df.end_date).resample('1W').sum().reset_index()
            df.loc[:,'end_time'] =df.end_date.values.astype(np.int64) // 10 ** 9 - 60*60*2
            return df.end_time.to_numpy(), df.completed.to_numpy()
        elif topic == 'Created Task':
            df = self.get_data_task()
            if filter_project != 'All':
                df = df.loc[df.project==filter_project]
            def count_created(serie):
                return len(serie)
            if freq == 'Daily':
                df = df.set_index(df.start_date).resample('1D').agg({'completed':count_created}).reset_index().completed.sum()
            else:
                df = df.set_index(df.start_date).resample('1W').agg({'completed':count_created}).reset_index().completed.sum()
            df.loc[:,'start_time'] =df.start_date.values.astype(np.int64) // 10 ** 9 - 60*60*2
            return df.start_time.to_numpy(), df.completed.to_numpy()
        elif topic == 'Completed Sub Project':
            df = self.get_data_subProject()
            if filter_project != 'All':
                df = df.loc[df.project==filter_project]
            if freq == 'Daily':
                df = df.set_index(df.end_date).resample('1d').sum().reset_index()
            else:
                df = df.set_index(df.end_date).resample('1W').sum().reset_index()
            df.loc[:,'end_time'] =df.end_date.values.astype(np.int64) // 10 ** 9 - 60*60*2
            return df.end_time.to_numpy(), df.completed.to_numpy()
        elif topic == 'Created Sub Project':
            df = self.get_data_subProject()
            if filter_project != 'All':
                df = df.loc[df.project==filter_project]
            def count_created(serie):
                return len(serie)
            if freq == 'Daily':
                df = df.set_index(df.start_date).resample('1D').agg({'completed':count_created}).reset_index().completed.sum()
            else:
                df = df.set_index(df.start_date).resample('1W').agg({'completed':count_created}).reset_index().completed.sum()
            df.loc[:,'start_time'] =df.start_date.values.astype(np.int64) // 10 ** 9 - 60*60*2
            return df.start_time.to_numpy(), df.completed.to_numpy()


    def get_arrays_ratio(self, filter_project, freq):
            df = self.get_data_task()
            def nbs_created(series):
                return (series == 1).sum()
            def nbs_completed(series):
                return len(series)
            df_created = df.set_index('start_date').resample('1w').agg({'completed':nbs_created}).reset_index()
            df_created = df_created.rename(columns={'start_date':'date','completed':'created'})
            df_completed = df.set_index('end_date').resample('1w').agg({'completed':nbs_created}).reset_index()
            df_completed = df_completed.rename(columns={'end_date':'date'})
            df = pd.merge(df_created, df_completed, how ='inner', on =['date']) 
            df.loc[:,'time'] = df.date.values.astype(np.int64) // 10 ** 9 - 60*60*2
            return df.created.to_numpy(), df.completed.to_numpy(), df.completed.to_numpy()


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
        self.checkBox_subProjectShowCompleted.setTristate(True)
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
        self.checkBox_TaskFilterShowCompleted.setTristate(True)
        self.groupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_13.setGeometry(QtCore.QRect(1160, 20, 431, 941))
        self.groupBox_13.setObjectName("groupBox_13")
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
        self.comboBox_statsProjectToPlot.setGeometry(QtCore.QRect(100, 37, 211, 22))
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
        # graph
        self.dockWidget = QtWidgets.QDockWidget(self.groupBox_13)
        self.dockWidget.setGeometry(QtCore.QRect(20, 110, 391, 281))
        self.dockWidget.setObjectName("widget_graphTemporel")
        # window
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Project

        # filter
        self.init_combo_filter_project()
        self.comboBox_projectFilterField.currentTextChanged.connect(self.refresh_tab_project)
        self.checkBox_projectShowComplete.stateChanged.connect(self.refresh_tab_project)

        # sort
        self.comboBox_projectSort.currentTextChanged.connect(self.refresh_tab_project)

        # new
        self.pushButton_projectCreate.clicked.connect(self.create_new_project)

    # sub project

        # filter
        self.comboBox_subProjectFilterField.currentTextChanged.connect(self.refresh_tab_subProject)
        self.checkBox_subProjectShowCompleted.stateChanged.connect(self.refresh_tab_subProject)

        # sort
        self.comboBox_subProjectSort.currentTextChanged.connect(self.refresh_tab_subProject)

        # new
        self.pushButton_subProjectCreate.clicked.connect(self.create_new_subProject)

    # Task

        # filter
        self.checkBox_TaskFilterShowCompleted.stateChanged.connect(self.refresh_tab_task)

        # sort
        self.comboBox_taskSort.currentTextChanged.connect(self.refresh_tab_task)

        # new
        self.pushButton_taskCreate.clicked.connect(self.create_new_task)

        self.refresh_tab_project()

    # stats
        #self.init_combo_filter_project()
        self.comboBox_statsTopictoPlot.currentTextChanged.connect(self.refresh_temporel_graph)
        self.comboBox_statsProjectToPlot.currentTextChanged.connect(self.refresh_temporel_graph)
        self.comboBox_statsFrequencyToPlot.currentTextChanged.connect(self.refresh_temporel_graph)
        self.checkBox_statsCumulativetoPlot.stateChanged.connect(self.refresh_temporel_graph)
        self.refresh_temporel_graph()

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(self._translate("MainWindow", "Project"))
        item = self.tableWidget_project.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "Done"))
        item = self.tableWidget_project.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "Project"))
        item = self.tableWidget_project.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "Field"))
        item = self.tableWidget_project.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "Goal"))
        item = self.tableWidget_project.horizontalHeaderItem(4)
        item.setText(self._translate("MainWindow", "Start Date"))
        item = self.tableWidget_project.horizontalHeaderItem(5)
        item.setText(self._translate("MainWindow", "Update Date"))
        item = self.tableWidget_project.horizontalHeaderItem(6)
        item.setText(self._translate("MainWindow", "% Done"))
        item = self.tableWidget_project.horizontalHeaderItem(7)
        item.setText(self._translate("MainWindow", "Delete"))
        self.groupBox_4.setTitle(self._translate("MainWindow", "Filters"))
        self.label.setText(self._translate("MainWindow", "Field:"))
        self.checkBox_projectShowComplete.setText(self._translate("MainWindow", "Show Completed"))
        self.groupBox_5.setTitle(self._translate("MainWindow", "Sort"))
        self.comboBox_projectSort.setItemText(0, self._translate("MainWindow", "Project"))
        self.comboBox_projectSort.setItemText(1, self._translate("MainWindow", "Field"))
        self.comboBox_projectSort.setItemText(2, self._translate("MainWindow", "Start Date"))
        self.comboBox_projectSort.setItemText(3, self._translate("MainWindow", "Update Date"))
        self.comboBox_projectSort.setItemText(4, self._translate("MainWindow", "% Done"))
        self.groupBox_8.setTitle(self._translate("MainWindow", "New"))
        self.pushButton_projectCreate.setText(self._translate("MainWindow", "Create New Project"))
        self.groupBox_2.setTitle(self._translate("MainWindow", "Sub Project of project:"))
        self.groupBox_6.setTitle(self._translate("MainWindow", "Filters"))
        self.label_3.setText(self._translate("MainWindow", "Sub Field:"))
        self.checkBox_subProjectShowCompleted.setText(self._translate("MainWindow", "Show Completed"))
        item = self.tableWidget_subProject.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "Done"))
        item = self.tableWidget_subProject.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "Sub Project"))
        item = self.tableWidget_subProject.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "Sub Field"))
        item = self.tableWidget_subProject.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "Goal"))
        item = self.tableWidget_subProject.horizontalHeaderItem(4)
        item.setText(self._translate("MainWindow", "Start Date"))
        item = self.tableWidget_subProject.horizontalHeaderItem(5)
        item.setText(self._translate("MainWindow", "Update Date"))
        item = self.tableWidget_subProject.horizontalHeaderItem(6)
        item.setText(self._translate("MainWindow", "% Done"))
        item = self.tableWidget_subProject.horizontalHeaderItem(7)
        item.setText(self._translate("MainWindow", "Delete"))
        self.groupBox_7.setTitle(self._translate("MainWindow", "Sort"))
        self.comboBox_subProjectSort.setItemText(0, self._translate("MainWindow", "Sub Project"))
        self.comboBox_subProjectSort.setItemText(1, self._translate("MainWindow", "Sub Field"))
        self.comboBox_subProjectSort.setItemText(2, self._translate("MainWindow", "Start Date"))
        self.comboBox_subProjectSort.setItemText(3, self._translate("MainWindow", "Update Date"))
        self.comboBox_subProjectSort.setItemText(4, self._translate("MainWindow", "% Done"))
        self.groupBox_9.setTitle(self._translate("MainWindow", "New"))
        self.pushButton_subProjectCreate.setText(self._translate("MainWindow", "Create Sub Project"))
        self.groupBox_3.setTitle(self._translate("MainWindow", "Task For Project:                                                 An Sub Project: "))
        self.groupBox_10.setTitle(self._translate("MainWindow", "Sort"))
        self.comboBox_taskSort.setItemText(0, self._translate("MainWindow", "Task"))
        self.comboBox_taskSort.setItemText(1, self._translate("MainWindow", "Start Date"))
        item = self.tableWidget_task.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "Done"))
        item = self.tableWidget_task.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "Task"))
        item = self.tableWidget_task.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "Goal"))
        item = self.tableWidget_task.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "Start Date"))
        item = self.tableWidget_task.horizontalHeaderItem(4)
        item.setText(self._translate("MainWindow", "Delete"))
        self.groupBox_11.setTitle(self._translate("MainWindow", "New"))
        self.pushButton_taskCreate.setText(self._translate("MainWindow", "Create Task"))
        self.groupBox_12.setTitle(self._translate("MainWindow", "Filters"))
        self.checkBox_TaskFilterShowCompleted.setText(self._translate("MainWindow", "Show Completed"))
        self.groupBox_13.setTitle(self._translate("MainWindow", "Statistics"))
        self.comboBox_statsTopictoPlot.setItemText(0, self._translate("MainWindow", "Completed Tasks"))
        self.comboBox_statsTopictoPlot.setItemText(1, self._translate("MainWindow", "Created Task"))
        self.comboBox_statsTopictoPlot.setItemText(2, self._translate("MainWindow", "Created Sub Project"))
        self.comboBox_statsTopictoPlot.setItemText(3, self._translate("MainWindow", "Completed Sub Project"))
        self.comboBox_statsFrequencyToPlot.setItemText(0, self._translate("MainWindow", "Weekly"))
        self.comboBox_statsFrequencyToPlot.setItemText(1, self._translate("MainWindow", "Daily"))
        self.checkBox_statsCumulativetoPlot.setText(self._translate("MainWindow", "Cumulative"))
        self.comboBox_statsProjectToPlot.setItemText(0, self._translate("MainWindow", "All"))
        self.label_5.setText(self._translate("MainWindow", "Project to plot:"))

# data
    
    def get_full_dict(self, name_project):
        print('loading dic',name_project)
        with open('data/{}.json'.format(name_project.replace(' ','_')),'r') as f:
            dic = json.load(f)
            f.close()
        return dic

    def dump_full_dict(self, dic, name_project):
        with open('data/{}.json'.format(name_project.replace(' ','_')),'w') as f:
            json.dump(dic, f)
            f.close()
        return dic

    def get_project_dict(self, name_project):
        dic = self.get_full_dict(name_project)
        return dic

    def get_subproject_dict(self, name_project, name_subProject):
        dic =  self.get_project_dict(name_project)
        return dic['sub_projects'][name_subProject]

    def post_project(self, name_project, field, goal):
        dic = {
            "name": name_project,
            "field": field,
            "goal": goal,
            "completed": False,
            "percent_completed": 0,
            "completed_date": "",
            "completed_time": "",
            "start_time": time.time(),
            "start_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "update_time": time.time(),
            "update_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "sub_projects": {}
        }
        self.dump_full_dict(dic, name_project)

    def post_subproject(self, name_project, name_subProject, subField, goal):
        dic = self.get_full_dict(name_project)
        dic["update_date"] = datetime.datetime.now().strftime('%Y-%m-%d')
        dic["update_time"] = time.time()
        new_dict = {name_subProject:{
            "name": name_subProject,
            "field": subField,
            "goal": goal,
            "completed": False,
            "percent_completed": 0,
            "completed_date": "",
            "completed_time": "",
            "start_time": time.time(),
            "start_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "update_time": time.time(),
            "update_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "tasks": {}
        }}
        dic["sub_projects"] = {**dic["sub_projects"], **new_dict}
        self.dump_full_dict(dic, name_project)

    def post_task(self, name_project, name_subProject, name_task, goal):
        dic = self.get_full_dict(name_project)
        if name_subProject in dic['sub_projects'].keys():
            dic["update_date"] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic["update_time"] = time.time()
            dic["sub_projects"][name_subProject]['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic["sub_projects"][name_subProject]["update_time"] = time.time()
            new_dict = {name_task:{
                "name": name_task,
                "goal": goal,
                "completed": False,
                "completed_date": "",
                "completed_time": "",
                "start_time": time.time(),
                "start_date": datetime.datetime.now().strftime('%Y-%m-%d')
            }}
            dic["sub_projects"][name_subProject]['tasks'] = {**dic["sub_projects"][name_subProject]['tasks'], **new_dict}
            self.dump_full_dict(dic, name_project)
        else:
            print('error in post tasks, ',name_subProject,'is not subproject in dic:\n',dic)

    def del_project(self, name_project):
        dic = self.get_full_dict(name_project)
        os.remove('data/{}.json'.format(name_project.replace(' ','_')))
        self.refresh_tab_project()


    def del_subproject(self, name_project, name_subProject):
        dic = self.get_full_dict(name_project)
        try:
            del dic['sub_projects'][name_subProject]
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def del_task(self, name_project, name_subProject, name_task):
        dic = self.get_full_dict(name_project)
        try:
            del dic['sub_projects'][name_subProject]["tasks"][name_task]
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    # edit goal

    def edit_project_goal(self, name_project, new_goal):
        dic = self.get_full_dict(name_project)
        try:
            dic['goal'] = new_goal
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    # calculate % done

    def get_project_percent_done(self, dic):
        #dic = self.get_full_dict(name_project)
        if len(dic["sub_projects"]) > 0:
            return len([key for key,item in dic["sub_projects"].items() if item["completed"]]) / len(dic["sub_projects"])
        else:
            return -1

    def get_subproject_percent_done(self, dic, name_subProject):
        #dic = self.get_full_dict(name_project)
        if len(dic["sub_projects"][name_subProject]['tasks']) > 0:
            return len([key for key,item in dic["sub_projects"][name_subProject]['tasks'].items() if item["completed"]]) / len(dic["sub_projects"][name_subProject]['tasks'])
        else:
            return -1

    # complete 

    def complete_project(self, name_project):
        dic = self.get_full_dict(name_project)
        try:
            if dic['completed']:
                dic['completed'] = False
            else:
                dic['completed'] = True
            dic['completed_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['completed_time'] = time.time()
            dic['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['update_time'] = time.time()
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def complete_sub_project(self, name_project, name_subProject):
        dic = self.get_full_dict(name_project)
        try:
            if dic['sub_projects'][name_subProject]['completed']:
                dic['sub_projects'][name_subProject]['completed'] = False
            else:
                dic['sub_projects'][name_subProject]['completed'] = True
            dic['sub_projects'][name_subProject]['completed_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['completed_time'] = time.time()
            # update
            dic['sub_projects'][name_subProject]['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['update_time'] = time.time()            
            dic['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['update_time'] = time.time()
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def complete_task(self, name_project, name_subProject, name_task):
        dic = self.get_full_dict(name_project)
        try:
            if dic['sub_projects'][name_subProject]['tasks'][name_task]['completed']:
                dic['sub_projects'][name_subProject]['tasks'][name_task]['completed'] = False
            else:
                dic['sub_projects'][name_subProject]['tasks'][name_task]['completed'] = True
            dic['sub_projects'][name_subProject]['tasks'][name_task]['completed_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['tasks'][name_task]['completed_time'] = time.time()
            # update
            dic['sub_projects'][name_subProject]['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['update_time'] = time.time()            
            dic['update_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
            dic['update_time'] = time.time()
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')


# Project

    # filter
    def init_combo_filter_project(self):
        # get all field
        list_field = []
        for filename in os.listdir('data'):
            with open('data/'+filename,'r') as f:
                dic = json.load(f)
                list_field.append(dic['field'].lower())
                f.close()
        list_field = list(np.unique(np.array(list_field)))
        # clear
        self.comboBox_projectFilterField.clear()
        self.comboBox_projectFilterField.addItem("")
        self.comboBox_projectFilterField.setItemText(self.comboBox_projectFilterField.count()-1, self._translate("MainWindow", str('No Filter')))
        for field in list_field:
            self.comboBox_projectFilterField.addItem("")
            self.comboBox_projectFilterField.setItemText(self.comboBox_projectFilterField.count()-1, self._translate("MainWindow", str(field)))


    # sort

    # new

    def create_new_project(self):
        print('openning dialog create project')
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_createProject() # place dialog object here
        ui.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            new_project_name = ui.new_project_name
            new_project_goal = ui.new_project_goal
            new_project_field = ui.new_project_field
            try:
                self.post_project(new_project_name, new_project_field, new_project_goal)
                self.refresh_tab_project()
                self.init_combo_filter_project()
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("ERROR")
                msgBox.setWindowTitle("error creating project "+new_project_name)
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                returnValue = msgBox.exec()
        else:
            print('dialog for new project have been closed') 

    # tab

    def refresh_tab_project(self):
        # extract filter & sort
        filter_field = self.comboBox_projectFilterField.currentText()
        filter_showCompleted = self.checkBox_projectShowComplete.checkState() # 0 => show only not colmpleted, 1=> show all 2=> show only completed
        sorter = self.comboBox_projectSort.currentText()
        print('filter is ',filter_field)
        # clear table
        while self.tableWidget_project.rowCount()>0:
            self.tableWidget_project.removeRow(self.tableWidget_project.rowCount()-1)
        # import all data
        list_project = []
        for filename in os.listdir('data'):
            with open('data/'+filename,'r') as f:
                dic = json.load(f)
                dic['percent_completed'] = self.get_project_percent_done(dic)
                #for name_subProject in dic['sub_projects'].keys():
                    #dic['sub_projects'][name_subProject]['percent_completed'] = self.get_subproject_percent_done(dic, name_subProject)
                list_project.append(dic)
                f.close()
        print('found ',len(list_project),'project')
        # apply filter
        if filter_field != 'No Filter' and filter_field != '':
            list_project = [dic for dic in list_project if dic['field'].lower()==filter_field.lower()]
        if filter_showCompleted == 0:
            list_project = [dic for dic in list_project if not dic['completed']]
        elif filter_showCompleted == 2:
            list_project = [dic for dic in list_project if dic['completed']]
        print('found ',len(list_project),'project')
        # order list
        if sorter == 'Project':
            list_project = sorted(list_project, key=lambda k: k['name'])
        elif sorter == 'Field':
            list_project = sorted(list_project, key=lambda k: k['field'])
        elif sorter == 'Start Date':
            list_project = sorted(list_project, key=lambda k: k['start_time'])
        elif sorter == 'Update Date':
            list_project = sorted(list_project, key=lambda k: k['update_time'])
        elif sorter == '% Done':
            list_project = sorted(list_project, key=lambda k: k['percent_completed'])
        # add new row
        for dict_project in list_project:
            current_row = self.tableWidget_project.rowCount()
            # create new row
            self.tableWidget_project.insertRow(current_row)
            #extract data
            isCompleted = dict_project['completed']
            name_project = dict_project['name']
            field = dict_project['field']
            goal = dict_project['goal']
            start_date = dict_project['start_date']
            update_date = dict_project['update_date']
            percent_completed = dict_project['percent_completed']
            # done
            tmp_checkbox_done = QtWidgets.QCheckBox(self.tableWidget_project)
            tmp_checkbox_done.setObjectName('checkBox_done_'+name_project)
            tmp_checkbox_done.setText(self._translate("MainWindow", ""))
            if isCompleted:
                tmp_checkbox_done.setCheckState(True)
            tmp_checkbox_done.stateChanged.connect(lambda x, name_project=name_project : self.table_complete_project(name_project))
            self.tableWidget_project.setCellWidget(current_row, 0, tmp_checkbox_done)
            # name
            tmp_pushButton_name = QtWidgets.QPushButton(self.tableWidget_project)
            tmp_pushButton_name.setObjectName('pushButt_name_'+name_project)
            tmp_pushButton_name.setText(self._translate("MainWindow", name_project))
            tmp_pushButton_name.clicked.connect(lambda x, name_project=name_project : self.table_open_project(name_project))
            self.tableWidget_project.setCellWidget(current_row, 1, tmp_pushButton_name)
            # field
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(field)))
            self.tableWidget_project.setItem(current_row, 2, item)
            # goal
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(goal)))
            self.tableWidget_project.setItem(current_row, 3, item)
            # start date
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(start_date)))
            self.tableWidget_project.setItem(current_row, 4, item)
            # update date
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(update_date)))
            self.tableWidget_project.setItem(current_row, 5, item)
            # percent done
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(int(100*percent_completed))+'%'))
            self.tableWidget_project.setItem(current_row, 6, item)
            # delete
            tmp_pushButton_name = QtWidgets.QCheckBox(self.tableWidget_project)
            tmp_pushButton_name.setObjectName('pushButt_del_'+name_project)
            tmp_pushButton_name.setText(self._translate("MainWindow", "delete"))
            tmp_pushButton_name.clicked.connect(lambda x, name_project=name_project : self.table_delete_project(name_project))
            self.tableWidget_project.setCellWidget(current_row, 7, tmp_pushButton_name)


    def table_complete_project(self, name_project):
        self.complete_project(name_project)
        self.refresh_tab_project()


    def table_open_project(self, name_project):
        print('opening project ', name_project)
        self.textBrowser_nameProject.setPlainText(name_project)
        self.textBrowser_nameProject2.setPlainText(name_project)
        self.init_combo_filter_subProject(name_project)
        self.refresh_tab_subProject()


    def table_delete_project(self, name_project):
        print('openning delete of ',name_project)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Are you sure about deleting project called '{}'?".format(name_project))
        msgBox.setWindowTitle("Deleting project "+name_project+'?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            self.del_project(name_project)
            self.refresh_tab_project()


# sub project

    # filter
    def init_combo_filter_subProject(self, name_project):
        dic = self.get_full_dict(name_project)
        # get all field
        list_field = []
        for key,item in dic['sub_projects'].items():
            list_field.append(item['field'])
        list_field = list(np.unique(np.array(list_field)))
        # clear
        self.comboBox_subProjectFilterField.addItem("")
        self.comboBox_subProjectFilterField.setItemText(self.comboBox_subProjectFilterField.count()-1, self._translate("MainWindow", str('No Filter')))
        for field in list_field:
            self.comboBox_subProjectFilterField.addItem("")
            self.comboBox_subProjectFilterField.setItemText(self.comboBox_subProjectFilterField.count()-1, self._translate("MainWindow", str(field)))

    # sort

    # new
    def create_new_subProject(self):
        print('openning dialog create sub project')
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_createSubProject() # place dialog object here
        ui.setupUi(dialog, self.textBrowser_nameProject.toPlainText())
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            new_subProject_name = ui.new_subProject_name
            new_subProject_goal = ui.new_subProject_goal
            new_subProject_field = ui.new_subProject_field
            try:
                current_project = self.textBrowser_nameProject.toPlainText()
                self.post_subproject(current_project, new_subProject_name, new_subProject_field, new_subProject_goal)
                self.refresh_tab_subProject()
                self.init_combo_filter_subProject(current_project)
            except Exception as e:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setWindowTitle("ERROR")
                msgBox.setText("error creating sub project "+new_subProject_name,'because of',str(e))
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                returnValue = msgBox.exec()
        else:
            print('dialog for new sub project have been closed') 

    # tab
    def refresh_tab_subProject(self):
        # extract filter & sort
        filter_field = self.comboBox_subProjectFilterField.currentText()
        filter_showCompleted = self.checkBox_subProjectShowCompleted.checkState() # 0 => show only not colmpleted, 1=> show all 2=> show only completed
        sorter = self.comboBox_subProjectSort.currentText()
        name_project = self.textBrowser_nameProject.toPlainText()
        # clear table
        while self.tableWidget_subProject.rowCount()>0:
            self.tableWidget_subProject.removeRow(self.tableWidget_subProject.rowCount()-1)
        # import all data
        dic_project = self.get_full_dict(name_project)
        list_project = [item for key,item in dic_project['sub_projects'].items()]
        for project in list_project:
            project['percent_completed'] = self.get_subproject_percent_done(dic_project, project['name'])
        # apply filter
        if filter_field != 'No Filter':
            list_project = [dic for dic in list_project if dic['field'].lower()==filter_field.lower()]
        if filter_showCompleted == 0:
            list_project = [dic for dic in list_project if not dic['completed']]
        elif filter_showCompleted == 2:
            list_project = [dic for dic in list_project if dic['completed']]
        # order list
        if sorter == 'Project':
            list_project = sorted(list_project, key=lambda k: k['name'])
        elif sorter == 'Field':
            list_project = sorted(list_project, key=lambda k: k['field'])
        elif sorter == 'Start Date':
            list_project = sorted(list_project, key=lambda k: k['start_time'])
        elif sorter == 'Update Date':
            list_project = sorted(list_project, key=lambda k: k['update_time'])
        elif sorter == '% Done':
            list_project = sorted(list_project, key=lambda k: k['percent_completed'])
        # add new row
        for dict_project in list_project:
            current_row = self.tableWidget_subProject.rowCount()
            # create new row
            self.tableWidget_subProject.insertRow(current_row)
            #extract data
            isCompleted = dict_project['completed']
            name_subProject = dict_project['name']
            field = dict_project['field']
            goal = dict_project['goal']
            start_date = dict_project['start_date']
            update_date = dict_project['update_date']
            percent_completed = dict_project['percent_completed']
            # done
            tmp_checkbox_done = QtWidgets.QCheckBox(self.tableWidget_subProject)
            tmp_checkbox_done.setObjectName('checkBox_done_sub_'+name_subProject)
            tmp_checkbox_done.setText(self._translate("MainWindow", ""))
            if isCompleted:
                tmp_checkbox_done.setCheckState(True)
            tmp_checkbox_done.stateChanged.connect(lambda x, name_project=name_project, name_subProject=name_subProject : self.table_complete_subProject(name_project, name_subProject))
            self.tableWidget_subProject.setCellWidget(current_row, 0, tmp_checkbox_done)
            # name
            tmp_pushButton_name = QtWidgets.QPushButton(self.tableWidget_subProject)
            tmp_pushButton_name.setObjectName('pushButt_name_sub_'+name_subProject)
            tmp_pushButton_name.setText(self._translate("MainWindow", name_subProject))
            tmp_pushButton_name.clicked.connect(lambda x, name_project=name_project, name_subProject=name_subProject : self.table_open_subProject(name_project, name_subProject))
            self.tableWidget_subProject.setCellWidget(current_row, 1, tmp_pushButton_name)
            # field
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(field)))
            self.tableWidget_subProject.setItem(current_row, 2, item)
            # goal
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(goal)))
            self.tableWidget_subProject.setItem(current_row, 3, item)
            # start date
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(start_date)))
            self.tableWidget_subProject.setItem(current_row, 4, item)
            # update date
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(update_date)))
            self.tableWidget_subProject.setItem(current_row, 5, item)
            # percent done
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(int(100*percent_completed))+'%'))
            self.tableWidget_subProject.setItem(current_row, 6, item)
            # delete
            tmp_pushButton_name = QtWidgets.QCheckBox(self.tableWidget_subProject)
            tmp_pushButton_name.setObjectName('pushButt_del_sub'+name_project)
            tmp_pushButton_name.setText(self._translate("MainWindow", "delete"))
            tmp_pushButton_name.clicked.connect(lambda x, name_project=name_project, name_subProject=name_subProject : self.table_delete_subProject(name_project, name_subProject))
            self.tableWidget_subProject.setCellWidget(current_row, 7, tmp_pushButton_name)

    def table_complete_subProject(self, name_project, name_subProject):
        self.complete_sub_project(name_project, name_subProject)
        self.refresh_tab_subProject()


    def table_open_subProject(self, name_project, name_subProject):
        print('opening sub project ', name_subProject)
        self.textBrowser_nameSubProject.setPlainText(name_subProject)
        self.refresh_tab_task()


    def table_delete_subProject(self, name_project, name_subProject):
        print('openning delete of ',name_subProject)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Are you sure about deleting sub project called '{}'?".format(name_subProject))
        msgBox.setWindowTitle("Deleting sub project "+name_subProject+'?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            self.del_subproject(name_project, name_subProject)
            self.refresh_tab_subProject()


# Task

    # filter

    # sort

    # new
    def create_new_task(self):
        print('openning dialog create task')
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_createTask() # place dialog object here
        ui.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            new_task_name = ui.textEdit_name.toPlainText()
            new_task_goal = ui.textEdit_goal.toPlainText()
            if True:
                current_project = self.textBrowser_nameProject.toPlainText()
                current_subProject = self.textBrowser_nameSubProject.toPlainText()
                self.post_task(current_project, current_subProject, new_task_name, new_task_goal)
                self.refresh_tab_task()
            if False:# Exception as e:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setWindowTitle("ERROR")
                msgBox.setText("error creating task "+new_task_name+'because of'+str(e))
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                returnValue = msgBox.exec()
        else:
            print('dialog for new task have been closed') 


    # tab
    def refresh_tab_task(self):
        print('refresh task')
        # extract filter & sort
        filter_showCompleted = self.checkBox_TaskFilterShowCompleted.checkState() # 0 => show only not colmpleted, 1=> show all 2=> show only completed
        sorter = self.comboBox_taskSort.currentText()
        name_project = self.textBrowser_nameProject.toPlainText()
        name_subProject = self.textBrowser_nameSubProject.toPlainText()
        # clear table
        while self.tableWidget_task.rowCount()>0:
            self.tableWidget_task.removeRow(self.tableWidget_task.rowCount()-1)
        # import all data
        dic_project = self.get_full_dict(name_project)
        dic_subProject = dic_project['sub_projects'][name_subProject]
        list_task = [item for key,item in dic_subProject['tasks'].items()]
        # apply filter
        if filter_showCompleted == 0:
            list_task = [dic for dic in list_task if not dic['completed']]
        elif filter_showCompleted == 2:
            list_task = [dic for dic in list_task if dic['completed']]
        # order list
        if sorter == 'Project':
            list_task = sorted(list_task, key=lambda k: k['name'])
        elif sorter == 'Start Date':
            list_task = sorted(list_task, key=lambda k: k['start_time'])
        # add new row
        for dict_task in list_task:
            current_row = self.tableWidget_task.rowCount()
            # create new row
            self.tableWidget_task.insertRow(current_row)
            #extract data
            isCompleted = dict_task['completed']
            name_task = dict_task['name']
            goal = dict_task['goal']
            start_date = dict_task['start_date']
            # done
            tmp_checkbox_done = QtWidgets.QCheckBox(self.tableWidget_task)
            tmp_checkbox_done.setObjectName('checkBox_done_task_'+name_subProject)
            tmp_checkbox_done.setText(self._translate("MainWindow", ""))
            if isCompleted:
                tmp_checkbox_done.setCheckState(True)
            tmp_checkbox_done.stateChanged.connect(lambda x, name_project=name_project, name_subProject=name_subProject, name_task=name_task : self.table_complete_task(name_project, name_subProject, name_task))
            self.tableWidget_task.setCellWidget(current_row, 0, tmp_checkbox_done)
            # name
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(name_task)))
            self.tableWidget_task.setItem(current_row, 1, item)
            # goal
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(goal)))
            self.tableWidget_task.setItem(current_row, 2, item)
            # start date
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", str(start_date)))
            self.tableWidget_task.setItem(current_row, 3, item)
            # delete
            tmp_pushButton_name = QtWidgets.QCheckBox(self.tableWidget_task)
            tmp_pushButton_name.setObjectName('pushButt_del_task_'+name_project)
            tmp_pushButton_name.setText(self._translate("MainWindow", "delete"))
            tmp_pushButton_name.clicked.connect(lambda x, name_project=name_project, name_subProject=name_subProject, name_task=name_task : self.table_delete_task(name_project, name_subProject, name_task))
            self.tableWidget_task.setCellWidget(current_row, 4, tmp_pushButton_name)

    def table_complete_task(self, name_project, name_subProject, name_task):
        self.complete_task(name_project, name_subProject, name_task)
        self.refresh_tab_task()


    def table_delete_task(self, name_project, name_subProject, name_task):
        print('openning task of ',name_task)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Are you sure about deleting task called '{}'?".format(name_project))
        msgBox.setWindowTitle("Deleting sub project "+name_subProject+'?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            self.del_task(name_project, name_subProject, name_task)
            self.refresh_tab_task()


# stats

    def refresh_temporel_graph(self):
        try:
            project_to_plot = self.comboBox_statsProjectToPlot.currentText() 
            topic_to_plot = self.comboBox_statsTopictoPlot.currentText()
            freq_to_plot = self.comboBox_statsFrequencyToPlot.currentText()
            cum_to_plot = self.checkBox_statsCumulativetoPlot.checkState()
            print(cum_to_plot,type(cum_to_plot))
            # project
            list_project = []
            for filename in os.listdir('data'):
                with open('data/'+filename,'r') as f:
                    dic = json.load(f)
                    list_project.append(dic)
                    f.close()
            # graph 1
            self.graphicView = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()})
            self.graphicView.enableAutoRange()
            self.graphicView.setBackground('w')
            x, y = DataExtractor().get_arrays(project_to_plot, topic_to_plot, freq_to_plot)
            if cum_to_plot == 2:
                y = y.cumsum()
                plot = self.graphicView.plot(x,y)
            else:
                bg = pg.BarGraphItem(x=x, height=y, width=0.3,brush='b')
                self.graphicView.addItem(bg)

            label_topic = topic_to_plot
            label_cum = {2:'cumulative ',0:''}[cum_to_plot]
            label_freq = freq_to_plot.lower()
            if project_to_plot == 'All':
                label_project = ''
            else:
                label_project = 'for project '+project_to_plot
            title = QtWidgets.QLabel()
            title.setText('{} {}{} {}'.format(label_topic, label_cum, label_freq, label_project))
            self.dockWidget.setTitleBarWidget(title)
            self.dockWidget.setWidget(self.graphicView)
        except Exception as e:
            print('cannot refresh graph because of '+str(e))
         


    def init_combo_filter_project(self):
        list_project = DataExtractor().get_list_project()
        self.comboBox_statsProjectToPlot.clear()
        self.comboBox_statsProjectToPlot.addItem("")
        self.comboBox_statsProjectToPlot.setItemText(self.comboBox_statsProjectToPlot.count()-1, self._translate("MainWindow", str('All')))
        for project in list_project:
            self.comboBox_statsProjectToPlot.addItem("")
            self.comboBox_statsProjectToPlot.setItemText(self.comboBox_statsProjectToPlot.count()-1, self._translate("MainWindow", str(project['name'])))


if __name__ == "__main__":
    # create necessary files & dir
    if 'data' not in os.listdir():
        os.mkdir('data')
    for filename in os.listdir('data'):
        if filename[-5:] != '.json':
            os.remove('data/'+filename)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
