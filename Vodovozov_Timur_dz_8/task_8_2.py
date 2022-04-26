import re


def parsing_file(file):
    pattern = re.compile(r'^(.+)\s-\s-\s\[(.+)]\s"(\w+[A-Z])\s(/\w+/\w+)\s.+"\s(\d+)\s(\d+)\s')
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            r = pattern.finditer(line)
            for i in r:
                result.append((i.group(1), i.group(2), i.group(3), i.group(4), i.group(5), i.group(6)))
    return result


f_list = parsing_file('nginx_logs.txt')
for el in f_list:
    print(el)
