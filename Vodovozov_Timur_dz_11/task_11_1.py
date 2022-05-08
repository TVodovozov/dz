class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        print(cls, date_as_string)
        return date

    @staticmethod
    def validate(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 4000:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = input(print('Введите дату: '))
date1 = Date.from_string(d)
is_date = Date.validate(d)
