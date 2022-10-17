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


def memory_dec(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_delta = m2[0] - m1[0]
        print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
        return res

    return wrapper


class Worker:
    @memory_dec
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    @memory_dec
    def get_full_name(self):
        return f'полное имя: {self.name} {self.surname}'

    @memory_dec
    def get_total_income(self):
        return f'общий доход: {sum(self._income.values())}'


programmer = Position('Иван', 'Иванов', 'программист', 20000, 70000)
print(programmer.get_full_name())
print(programmer.position)
print(programmer.get_total_income())


class WorkerOptimized:
    @memory_dec
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class PositionOptimized(WorkerOptimized):
    __slots__ = ('name', 'surname', 'position', 'wage', 'bonus')

    @memory_dec
    def get_full_name_optimized(self):
        return f'полное имя: {self.name} {self.surname}'

    @memory_dec
    def get_total_income_optimized(self):
        return f'общий доход: {sum(self._income.values())}'


programmer = PositionOptimized('Иван', 'Иванов', 'программист', 20000, 70000)
print(programmer.get_full_name_optimized())
print(programmer.position)
print(programmer.get_total_income_optimized())

"""
Выполнение __init__ использовало 0.0078125 Mib
Выполнение get_full_name использовало 0.0 Mib
полное имя: Иван Иванов
программист
Выполнение get_total_income использовало 0.0 Mib
общий доход: 90000

Выполнение __init__ использовало 0.0 Mib
Выполнение get_full_name_optimized использовало 0.0 Mib
полное имя: Иван Иванов
программист
Выполнение get_total_income_optimized использовало 0.0 Mib
общий доход: 90000

При использовании __slots__ наблюдается значительная оптимизация динамической памяти
"""