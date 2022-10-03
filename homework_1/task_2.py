"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# Сложность первого алгоритма должна быть O(n^2) - квадратичная.


def min_value_of_list_1(list_value):
    min_value = list_value[0]  # O(1)
    for i in list_value:  # O(n)
        for j in range(list_value.index(i) + 1, len(list_value) - 1, 1):  # O(n)
            if min_value > list_value[j]:  # O(1)
                min_value = list_value[j]  # O(1)
    return min_value  # O(1)


# Сложность второго алгоритма должна быть O(n) - линейная.


def min_value_of_list_2(list_value):
    min_value = list_value[0]  # O(1)
    for i in range(len(list_value)):  # O(n)
        if list_value[i] < min_value:  # O(1)
            min_value = list_value[i]  # O(1)
    return min_value  # O(1)


lst = (1, 4, 5)

print(min_value_of_list_2(lst))
print(min_value_of_list_1(lst))
