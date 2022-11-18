"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


arr = [i for i in range(100)]
print(timeit('func_1(arr)', globals=globals(), number=1000))

'''
0.0078381
'''


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit('func_2(arr)', globals=globals(), number=1000))

'''
0.006396699999999991
Что бы создать и заполнить массив одновременно я использовал List Comprehension это ускорило работу func_2.
'''
