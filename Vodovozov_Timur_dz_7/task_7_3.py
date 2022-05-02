import os
import shutil

ROOT = os.path.join(os.path.dirname(__file__), 'my_project')
DIR = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(DIR):
    os.makedirs(DIR)
for root, dirs, files in os.walk(ROOT):
    if root.count('templates'):
        for el in dirs:
            if not os.path.exists(os.path.join(DIR, el)):
                os.makedirs(os.path.join(DIR, el))
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(DIR, os.path.basename(root))
            if not os.path.dirname(src_file) == dst_file:
                shutil.copy(src_file, dst_file)
