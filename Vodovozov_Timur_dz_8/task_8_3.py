def type_logger(func):
    def wrapper(*args):
        calc = func(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for el in args:
                print(f'{el}: {type(el)} ')
        return calc

    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


a = calc_cube(3, 5, 7)
print(a)
