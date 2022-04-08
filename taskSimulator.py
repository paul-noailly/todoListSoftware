import numpy as np, pandas as pd, datetime, time, json, os, matplotlib.pyplot as plt

class TaskSimulator():
    def __init__(self, init_time, end_time, daily_new_project, daily_new_subproject, daily_new_task, daily_complete_task, daily_complete_subproject, daily_complete_project, proba_new_field, proba_new_subField,do_reset):
        for filename in os.listdir('data'):
            if do_reset:
                os.remove('data/'+filename)
        self.init_time = init_time
        self.end_time = end_time
        self.daily_new_project = daily_new_project
        self.daily_new_subproject = daily_new_subproject
        self.daily_new_task = daily_new_task
        self.daily_complete_task = daily_complete_task
        self.daily_complete_subproject = daily_complete_subproject
        self.daily_complete_project = daily_complete_project

        self.proba_new_field = proba_new_field
        self.proba_new_subField = proba_new_subField

        self.list_field = []
        self.list_subField = []

        self.list_completed_project = []
        self.list_completed_subproject = []
    
    # data
    
    def get_full_dict(self, name_project):
        #print('loading dic',name_project)
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

    def post_project(self, name_project, field, goal, time_post):
        dic = {
            "name": name_project,
            "field": field,
            "goal": goal,
            "completed": False,
            "percent_completed": 0,
            "completed_date": "",
            "completed_time": "",
            "start_time": time_post,
            "start_date": datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d'),
            "update_time": time_post,
            "update_date": datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d'),
            "sub_projects": {}
        }
        self.dump_full_dict(dic, name_project)

    def post_subproject(self, name_project, name_subProject, subField, goal, time_post):
        dic = self.get_full_dict(name_project)
        dic["update_date"] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
        dic["update_time"] = time_post
        new_dict = {name_subProject:{
            "name": name_subProject,
            "field": subField,
            "goal": goal,
            "completed": False,
            "percent_completed": 0,
            "completed_date": "",
            "completed_time": "",
            "start_time": time_post,
            "start_date": datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d'),
            "update_time": time_post,
            "update_date": datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d'),
            "tasks": {}
        }}
        dic["sub_projects"] = {**dic["sub_projects"], **new_dict}
        self.dump_full_dict(dic, name_project)

    def post_task(self, name_project, name_subProject, name_task, goal, time_post):
        dic = self.get_full_dict(name_project)
        if name_subProject in dic['sub_projects'].keys():
            dic["update_date"] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic["update_time"] = time_post
            dic["sub_projects"][name_subProject]['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic["sub_projects"][name_subProject]["update_time"] = time_post
            new_dict = {name_task:{
                "name": name_task,
                "goal": goal,
                "completed": False,
                "completed_date": "",
                "completed_time": "",
                "start_time": time_post,
                "start_date": datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
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

    def complete_project(self, name_project, time_post):
        dic = self.get_full_dict(name_project)
        try:
            if dic['completed']:
                dic['completed'] = False
            else:
                dic['completed'] = True
            dic['completed_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['completed_time'] = time_post
            dic['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['update_time'] = time_post
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def complete_sub_project(self, name_project, name_subProject, time_post):
        dic = self.get_full_dict(name_project)
        try:
            if dic['sub_projects'][name_subProject]['completed']:
                dic['sub_projects'][name_subProject]['completed'] = False
            else:
                dic['sub_projects'][name_subProject]['completed'] = True
            dic['sub_projects'][name_subProject]['completed_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['completed_time'] = time_post
            # update
            dic['sub_projects'][name_subProject]['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['update_time'] = time_post            
            dic['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['update_time'] = time_post
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def complete_task(self, name_project, name_subProject, name_task, time_post):
        dic = self.get_full_dict(name_project)
        try:
            if dic['sub_projects'][name_subProject]['tasks'][name_task]['completed']:
                dic['sub_projects'][name_subProject]['tasks'][name_task]['completed'] = False
            else:
                dic['sub_projects'][name_subProject]['tasks'][name_task]['completed'] = True
            dic['sub_projects'][name_subProject]['tasks'][name_task]['completed_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['tasks'][name_task]['completed_time'] = time_post
            # update
            dic['sub_projects'][name_subProject]['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['sub_projects'][name_subProject]['update_time'] = time_post            
            dic['update_date'] = datetime.datetime.fromtimestamp(time_post).strftime('%Y-%m-%d')
            dic['update_time'] = time_post
            self.dump_full_dict(dic, name_project)
        except:
            print('error\n',dic,'\n')

    def get_list_project(self):        
        list_project = []
        for filename in os.listdir('data'):
            with open('data/'+filename,'r') as f:
                dic = json.load(f)
                list_project.append(dic)
                f.close()
        return list_project

    def run(self):
        time_post = self.init_time
        self.exec_event_dic({"new_project":True,"new_subproject": True,"new_task": True,"complete_project": False,"complete_subproject": False,"complete_task": False},time_post)
        self.exec_event_dic({"new_project":True,"new_subproject": True,"new_task": True,"complete_project": False,"complete_subproject": False,"complete_task": False},time_post)
        while time_post < self.end_time:    
            time_post += 60*60
            self.exec_event_dic(self.get_event_dict(), time_post)

    def get_event_dict(self):
        def doEvent(proba):
            if np.random.random() > 1 - proba:
                return True
            return False
        res = {
            "new_project": doEvent(self.daily_new_project/24),
            "new_subproject": doEvent(self.daily_new_subproject/24),
            "new_task": doEvent(self.daily_new_task/24),
            "complete_project": doEvent(self.daily_complete_project/24),
            "complete_subproject": doEvent(self.daily_complete_subproject/24),
            "complete_task": doEvent(self.daily_complete_task/24)
        }
        return res

    def exec_event_dic(self, event_dic, time_post):
        # new project
        if event_dic['new_project']:
            list_project = self.get_list_project()
            if np.random.random()>self.proba_new_field or len(self.list_field)==0:
                field = 'field_'+str(len(self.list_field))
                self.list_field.append(field)
            else:
                field = np.random.choice(self.list_field)
            self.post_project('project_'+str(len(list_project)), field, 'goal_'+str(len(list_project)), time_post)
            print('[{}] - new project    : {}'.format(datetime.datetime.fromtimestamp(time_post),'project_'+str(len(list_project))))

        # new subproject
        if event_dic['new_subproject']:
            list_project = self.get_list_project()
            list_project_not_completed = [dic['name'] for dic in list_project if dic['name'] not in self.list_completed_project]
            if len(list_project_not_completed) > 0:
                name_project = np.random.choice(list_project_not_completed)
                dic_project = self.get_full_dict(name_project) 
                name_subProject = 'subProject_'+str(len(dic_project['sub_projects']))
                if np.random.random()>self.proba_new_subField or len(self.list_subField)==0:
                    subField = 'field_'+str(len(self.list_subField))
                    self.list_subField.append(subField)
                else:
                    subField = np.random.choice(self.list_subField)
                goal = 'goal_'+str(len(dic_project['sub_projects']))
                self.post_subproject(name_project, name_subProject, subField, goal, time_post)
                print('[{}] - new subproject : {} - {}'.format(datetime.datetime.fromtimestamp(time_post),name_project, name_subProject))

        # new task
        if event_dic['new_task']:
            list_project = self.get_list_project()
            list_project_not_completed = [dic['name'] for dic in list_project if dic['name'] not in self.list_completed_project]
            if len(list_project_not_completed) > 0:
                name_project = np.random.choice(list_project_not_completed)
                dic_project = self.get_full_dict(name_project) 
                list_subproject_not_completed = [item['name'] for key,item in dic_project['sub_projects'].items() if name_project+item['name'] not in self.list_completed_subproject]
                if len(list_subproject_not_completed) > 0:
                    name_subProject = np.random.choice(list_subproject_not_completed)
                    name_task = 'task_'+str(len(dic_project['sub_projects'][name_subProject]['tasks']))
                    goal = 'goal_'+str(len(dic_project['sub_projects'][name_subProject]['tasks']))
                    self.post_task(name_project, name_subProject, name_task, goal, time_post)

        # project
        if event_dic['complete_project']:
            list_project = self.get_list_project()
            if len([dic['name'] for dic in list_project if not dic['completed']]) > 1:
                list_project_not_completed = [dic['name'] for dic in list_project if dic['name'] not in self.list_completed_project]
                if len(list_project_not_completed) > 1:
                    name_project = np.random.choice(list_project_not_completed)
                    self.list_completed_project.append(name_project)
                    self.complete_project(name_project, time_post)

        # new complete sub project
        if event_dic['complete_subproject']:
            list_project = self.get_list_project()
            list_project_not_completed = [dic for dic in list_project if not dic['completed']]
            list_projectsubproject_not_completed = []
            for project in list_project_not_completed:
                for key,item in project['sub_projects'].items():
                    if not item['completed']:
                        list_projectsubproject_not_completed.append(project['name']+'|'+item['name'])
            if len(list_projectsubproject_not_completed) > 2:
                choice = np.random.choice(list_projectsubproject_not_completed)
                name_project, name_subProject = choice.split('|')[0], choice.split('|')[1] 
                self.list_completed_subproject.append(name_project+name_subProject)
                self.complete_sub_project(name_project, name_subProject, time_post)

        # new complete task
        if event_dic['complete_task']:
            list_project = self.get_list_project()
            list_project_not_completed = [dic for dic in list_project if not dic['completed']]
            list_projectsubprojecttask_not_completed = []
            for project in list_project_not_completed:
                for key,item in project['sub_projects'].items():
                    if not item['completed']:
                        for name_task in [itemTask['name'] for keyTask,itemTask in item['tasks'].items() if not itemTask['completed']]:
                            list_projectsubprojecttask_not_completed.append(project['name']+'|'+item['name']+'|'+ name_task)
            if len(list_projectsubprojecttask_not_completed) > 2:
                choice = np.random.choice(list_projectsubprojecttask_not_completed)
                name_project, name_subProject, name_task = choice.split('|')[0], choice.split('|')[1], choice.split('|')[2]
                self.complete_task(name_project, name_subProject, name_task, time_post)

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




















from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):#, Ui_StartForm):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # dock
        self.dockWidget = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget.setGeometry(QtCore.QRect(0, 50, 400, 300))
        
        MainWindow.setCentralWidget(self.centralwidget)
        # graph view
        self.graphicView = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()})
        self.graphicView.enableAutoRange()
        self.graphicView.setBackground('w')
        #self.verticalLayout.addWidget(self.graphicsView)     
        
        
        
        
        y = [1, 3, 2, 4, 6, 5, 3]
        x = [1,2,3,4,5,6,7]
        
        
        
        
        
        
        
        plot = self.graphicView.plot(x,y)
        self.dockWidget.setWidget(self.graphicView)

if __name__ == '__main__' and False:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


