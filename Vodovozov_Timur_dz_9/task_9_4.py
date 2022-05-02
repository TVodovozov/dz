class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {"направо" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'скорость машины {self.name} {self.speed}')


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля {self.speed}. Превышение скорости' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля {self.speed}. Превышение скорости' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля: {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


police_car = PoliceCar('Лада', 90, 'синий')
police_car.go()
police_car.turn(0)
print(police_car.show_speed())
police_car.stop()

work_car = WorkCar('Газель', 45, 'белая')
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.stop()

town_car = TownCar('Тойота', 60, 'красная')
town_car.go()
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
