"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


def new_array(length):
    arr = []
    for _ in range(length):
        arr.append(randint(-100, 100))
    return arr


def bubble_sort_increasing(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_decreasing(arr):
    for i in range(len(arr)):
        is_sorted = True
        for j in range(len(arr) - i - 1):
            if arr[-j - 1] < arr[-j - 2]:
                arr[-j - 1], arr[-j - 2] = arr[-j - 2], arr[-j - 1]
                is_sorted = False
        if is_sorted:
            break
    return arr


size = 10

print(bubble_sort_increasing(new_array(size)[:]))
print(bubble_sort_decreasing(new_array(size)[:]))
print(new_array(size))
print('*' * 50)

"""
[-92, 10, 27, 33, 34, 34, 78, 80, 94, 96]
[-80, -77, -62, -55, -35, 8, 12, 24, 81, 87]
[16, 70, -12, 40, -16, 56, -5, 58, -25, -26]
"""


for d in range(1, 4):
    my_array = new_array(size ** d)
    print(f'Массив из {size ** d} элементов: ')
    print(f'Время для функции bubble_sort_increasing: '
          f'{timeit("bubble_sort_increasing(my_array[:])", globals=globals(), number=1000)}')
    print(f'Время для функции bubble_sort_decreasing: '
          f'{timeit("bubble_sort_decreasing(my_array[:])", globals=globals(), number=1000)}')
    print('*' * 50)

"""
**************************************************
Массив из 10 элементов: 
Время для функции bubble_sort_increasing: 0.014111800000000008
Время для функции bubble_sort_decreasing: 0.014861699999999992
**************************************************
Массив из 100 элементов: 
Время для функции bubble_sort_increasing: 0.6863322000000001
Время для функции bubble_sort_decreasing: 1.4510824
**************************************************
Массив из 1000 элементов: 
Время для функции bubble_sort_increasing: 71.30533670000001
Время для функции bubble_sort_decreasing: 157.00198160000002
**************************************************

Доработка функции очень помогла, время значительно ускорилось
"""