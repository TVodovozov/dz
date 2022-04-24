import os

values = ['settings', 'mainapp', 'adminapp', 'authapp']
keys = 'my_project'
my_dict = {keys: values}

dir_path = [os.makedirs(os.path.join(keys, i)) for i in values if not os.path.exists(os.path.join(keys, i))]
