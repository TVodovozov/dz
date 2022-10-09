"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_4():
    max_dict = {i: array.count(i) for i in set(array)}
    elem = max(max_dict, key=lambda x: max_dict[x])
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_5():
    elem = max(map(lambda val: (array.count(val), val), set(array)))[1]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_6():
    elem = max(set(array), key=lambda x: array.count(x))
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
print(func_6())

print('Время первой функции: ', timeit('func_1()', globals=globals(), number=1000))
print('Время второй функции: ', timeit('func_2()', globals=globals(), number=1000))
print('Время третей функции: ', timeit('func_3()', globals=globals(), number=1000))
print('Время четвертой функции: ', timeit('func_4()', globals=globals(), number=1000))
print('Время пятой функции: ', timeit('func_5()', globals=globals(), number=1000))
print('Время шестой функции: ', timeit('func_6()', globals=globals(), number=1000))

'''
Время первой функции:  0.001363000000000003
Время второй функции:  0.0018179000000000112
Время третей функции:  0.0019398999999999944
Время четвертой функции:  0.0022132000000000124
Время пятой функции:  0.0018602999999999953
Время шестой функции:  0.0017694999999999933
Реализовал 4 разных решения поиска частоты числа, которое встречается в массиве чаще всего, 
в 6 функции удалось выйти на почетное второе место по скорости.
'''
