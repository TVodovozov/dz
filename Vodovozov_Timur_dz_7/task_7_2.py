import os
import json

ROOT = os.path.dirname(__file__)

with open('config.json', 'r', encoding='utf-8') as f:
    list_dir = json.load(f)
for dir_path in list_dir:
    full_dir_path = os.path.join(ROOT, dir_path)
    os.makedirs(full_dir_path, exist_ok=True)
    for file_name in list_dir[dir_path]:
        with open(os.path.join(full_dir_path, file_name), 'x', encoding='utf-8'):
            pass
