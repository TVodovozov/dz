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
from memory_profiler import memory_usage
from random import randint


def memory_dec(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_delta = m2[0] - m1[0]
        print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
        return res

    return wrapper


nums = [randint(0, 10000) for i in range(10000)]


@memory_dec
def func_1():
    m = 0
    num = 0
    for i in nums:
        count = nums.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memory_dec
def func_2():
    new_array = []
    for el in nums:
        count2 = nums.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = nums[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@memory_dec
def func_3():
    elem = max(nums, key=lambda x: nums.count(x))
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {nums.count(elem)} раз(а)'


@memory_dec
def func_4():
    max_dict = {i: nums.count(i) for i in set(nums)}
    elem = max(max_dict, key=lambda x: max_dict[x])
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {nums.count(elem)} раз(а)'


@memory_dec
def func_5():
    elem = max(map(lambda val: (nums.count(val), val), set(nums)))[1]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {nums.count(elem)} раз(а)'


@memory_dec
def func_6():
    elem = max(set(nums), key=lambda x: nums.count(x))
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {nums.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
print(func_6())

"""
Выполнение func_1 использовало 0.0078125 Mib
Чаще всего встречается число 9466, оно появилось в массиве 6 раз(а)

Выполнение func_2 использовало 0.07421875 Mib
Чаще всего встречается число 9466, оно появилось в массиве 6 раз(а)

Выполнение func_3 использовало 0.0 Mib
Чаще всего встречается число 9466, оно появилось в массиве 6 раз(а)

Выполнение func_4 использовало 0.09375 Mib
Чаще всего встречается число 521, оно появилось в массиве 6 раз(а)

Выполнение func_5 использовало 0.0 Mib
Чаще всего встречается число 9466, оно появилось в массиве 6 раз(а)

Выполнение func_6 использовало 0.0 Mib
Чаще всего встречается число 521, оно появилось в массиве 6 раз(а)


При использовании lambda функции наблюдается значительная оптимизация динамической памяти
"""
