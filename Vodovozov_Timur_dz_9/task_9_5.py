class Stationary:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Начнем рисовать {self.title} ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Начнем рисовать {self.title} карандашем')


class Handle(Stationary):
    def draw(self):
        print(f'Начнем рисовать {self.title} маркером')


stationary = Stationary()
stationary.draw()
pen = Pen('синией')
pen.draw()
pencil = Pencil('простым')
pencil.draw()
handle = Handle('черным')
handle.draw()
