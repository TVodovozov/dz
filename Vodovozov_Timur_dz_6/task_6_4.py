import sys

with open('users.csv', 'r', encoding='utf-8') as file_1, \
        open('hobby.csv', 'r', encoding='utf-8') as file_2, \
        open('hobby_users.txt', 'w', encoding='utf-8') as file_3:
    for line_1 in file_1:
        line_2 = file_2.readline().strip()
        if not line_2:
            line_2 = None
        file_3.write(f'{line_1.strip()} : {line_2}\n')
    content = file_2.readline()
    if content:
        sys.exit(1)
print()
