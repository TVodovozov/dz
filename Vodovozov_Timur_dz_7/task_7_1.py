import os


dir_name = 'my_project'
file_name = ''
if not os.path.exists(dir_name):
    os.mkdir(dir_name)