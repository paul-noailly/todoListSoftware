import os

for filename in os.listdir('raw_ui'):
    if filename[-3:] == '.ui':
        print('extracting',filename[:-3])
        os.system('pyuic5 -x {} -o {}.py'.format('raw_ui/'+filename,'raw_ui/'+filename[:-3]))