"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        lst = []
        for i in range(len(self.elems)):
            if len(self.elems[i]) < 5:
                self.elems[i].append(el)
        return self.elems.append(lst)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item


if __name__ == '__main__':
    stack = StackClass()
    i = 0
    while i <= 20:
        stack.push_in(i)
        i += 1

    print(stack.elems)
