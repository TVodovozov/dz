import sys
import json

d = dict()
with open('users.csv', 'r', encoding='utf-8') as file_1, \
        open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for line_1 in file_1:
        line_2 = file_2.readline().strip()
        if not line_2:
            line_2 = None
        if line_1 not in d:
            d[line_1.strip()] = line_2
    connect = file_2.read()
    if connect:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as file_result:
    dict_as_str = json.dumps(d, ensure_ascii=False)
    file_result.write(dict_as_str)
with open('result.json', 'r', encoding='utf-8') as file_3:
    connect = file_3.read()
    result = json.loads(connect)
print(result)
