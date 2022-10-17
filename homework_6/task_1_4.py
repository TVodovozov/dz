"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для первого скрипта
"""

from memory_profiler import profile, memory_usage
import numpy as np
from random import randint
from timeit import timeit


def memory_dec(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_delta = m2[0] - m1[0]
        print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
        return res

    return wrapper


@profile
@memory_dec
def list_append():
    my_list = []
    for i in range(100000):
        my_list.append(randint(1, 1000))


@profile
@memory_dec
def array_append():
    my_array = np.array([])
    for i in range(100000):
        np.append(my_array, randint(1, 1000))


print(f'Время выполнения: ', timeit("list_append()", setup="from __main__ import list_append", number=1))
print(f'Время выполнения: ', timeit("array_append()", setup="from __main__ import array_append", number=1))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    33     30.8 MiB     30.8 MiB           1       def wrapper(*args):
    34     30.8 MiB      0.0 MiB           1           m1 = memory_usage()
    35     32.5 MiB      1.7 MiB           1           res = func(*args)
    36     32.5 MiB      0.0 MiB           1           m2 = memory_usage()
    37     32.5 MiB      0.0 MiB           1           mem_delta = m2[0] - m1[0]
    38     32.5 MiB      0.0 MiB           1           print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
    39     32.5 MiB      0.0 MiB           1           return res


Время выполнения: 2.2653392
Выполнение list_append использовало 1.71484375 Mib


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    33     32.5 MiB     32.5 MiB           1       def wrapper(*args):
    34     32.5 MiB      0.0 MiB           1           m1 = memory_usage()
    35     32.5 MiB      0.0 MiB           1           res = func(*args)
    36     32.5 MiB      0.0 MiB           1           m2 = memory_usage()
    37     32.5 MiB      0.0 MiB           1           mem_delta = m2[0] - m1[0]
    38     32.5 MiB      0.0 MiB           1           print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
    39     32.5 MiB      0.0 MiB           1           return res


Время выполнения: 5.1441943
Выполнение array_append использовало 0.0 Mib

Array из библиотеки Numpy занимает меньше места в памяти, но при этом заполняются медленнее, чем списки.
"""
