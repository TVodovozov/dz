import os

directory = os.path.join(os.path.dirname(__file__), 'some_data')
groups = [100, 1000, 10000, 100000]
result = dict.fromkeys(groups, 0)

for dirs, sub_dir, files in os.walk(directory):
    for file in files:
        path = os.path.join(dirs, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1

prev_size = 0
for size in groups:
    print(f"{size:10} : {result[size]}")
