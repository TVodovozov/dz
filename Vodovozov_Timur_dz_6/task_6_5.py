# coding: utf-8
import sys

row_num = int(sys.argv[1])
value = sys.argv[2]
len_row = 14

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    if f.seek((row_num - 1) * len_row) > f.seek(0, 2):
        print(f'Номер записи {row_num} не существует.')
    else:
        f.seek((row_num - 1) * len_row)
        f.write(f'{value:>12}\n')
