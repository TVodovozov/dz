class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row_len):
        result = ['*' * row_len] * (self.nums // row_len)
        if self.nums % row_len:
            result.append('*' * (self.nums % row_len))
            return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сумма ячеек равна: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Разница ячеек равна: ')
        if self.nums < other.nums:
            raise ValueError('Ячеек в первой клетке меньше, чем во второй')
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        print('Произведение ячеек равно: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Деление ячеек равно: ')
        return Cell(self.nums // other.nums)


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
