class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def calculation_of_mass(self):
        length = self._length
        width = self._width
        weight = self.weight
        depth = self.depth
        result = length * width * weight * depth / 1000
        return print(f"Масса асфальта: {length} м * {width} м * {weight} кг * {depth} см = ", result, "т")


r = Road(20, 5000, 25, 5)
r.calculation_of_mass()
