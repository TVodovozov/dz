"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i ** 2 for i in range(10000)}
my_ordered_dict = OrderedDict({i: i ** 2 for i in range(10000)})


def change_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict[i] = i
    return some_dict_orderdict


def pop_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict.pop(i)
    return some_dict_orderdict


print('Изменение dict: ', timeit('pop_dict(my_dict.copy())', globals=globals(), number=100))
print('Изменение Ordereddict: ', timeit('pop_dict(my_ordered_dict.copy())', globals=globals(), number=100), '\n')

print('Удаление dict: ', timeit('pop_dict(my_dict.copy())', globals=globals(), number=100))
print('Удаление Ordereddict: ', timeit('pop_dict(my_ordered_dict.copy())', globals=globals(), number=100))

'''
Изменение dict:  0.0910929
Изменение Ordereddict:  0.3833468 

Удаление dict:  0.16316540000000002
Удаление Ordereddict:  0.3700534000000001

Выполнение операций изменения и удаления в обычном dict происходит намного быстрее, чем с OrderedDict.
Пока нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях.
'''
