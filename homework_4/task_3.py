"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num  # исправлено
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)  # исправлено


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = int((revers_num + num / 10) * 10)  # исправлено
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, revers_num=''):
    if enter_num > 0:
        revers_num, enter_num = f'{revers_num}{enter_num % 10}', enter_num // 10
        return revers_4(enter_num, revers_num)
    return revers_num


my_nums = 123
print('Время первой функции: ', timeit('revers(my_nums)', globals=globals(), number=1000))
print('Время второй функции: ', timeit('revers_2(my_nums)', globals=globals(), number=1000))
print('Время третей функции: ', timeit('revers_3(my_nums)', globals=globals(), number=1000))
print('Время четвертой функции: ', timeit('revers_4(my_nums)', globals=globals(), number=1000))

'''
Время первой функции:  0.0007623999999999964
Время второй функции:  0.0011469999999999952
Время третей функции:  0.0003212999999999966
Время четвертой функции:  0.0009385999999999978

Функция три (revers_3) работает быстрее всех потому, что при помощи среза копируется вся строка в обратном порядке, 
а так же сложность O(n) самая маленькая из всех.
'''
