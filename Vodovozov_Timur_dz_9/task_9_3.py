class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'общий доход: {sum(self._income.values())}'


programmer = Position('Иван', 'Иванов', 'программист', 20000, 70000)
print(programmer.get_full_name())
print(programmer.position)
print(programmer.get_total_income())
