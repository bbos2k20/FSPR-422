def somethings():  # функция
    print("hello")


# Вызов функции
print("вызов функции", somethings())


def somethings():
    return "Hello"  # return - возврощает


result = somethings
print(result)


def somethings(name):
    print(f"Hello {name}")


somethings("abbos")
s = "abbos"
somethings(s)
somethings(input("ВВЕДИТЕ ИМЯ: "))


def somethings(name):
    return f"hello {name}"


print(somethings("xumo"))
result = somethings("jam")
print(result)


faranheits = [20, 19, 24, 45]


def fars_to_cels(faranheits):
    result = []
    for far in faranheits:
        celsius = (faran - 32) * 5 / 9
        result.append(celsius)
    return result


print(fars_to_cels(faranheits))

for faran in faranheits:
    celsius = (faran - 32) * 5 / 9
    if celsius >= 50:
        print("ЖАРААА")
        continue
    elif celsius <= 5:
        print("очень холодно")
    else:
        print("жить можно")
    print("celsius =", celsius, "faranheit =", faran)

    result.append(celsius)


def square():

    square_line = 4
    star = "*"

    def draw_square(square_line, star):
        for i in range(square_line):
            if i > 0 and i < (square_line - 1):  # i < 0 and i < 5; i = 1 2 3 4
                empty_space = " " * (square_line - 2)  # 4 "  "
                print(f"{star}{empty_space}{star}")
            else:
                print(star * square_line)

    draw_square(10, "_")


class Square:
    def __init__(self, side):
        self.side = side

    def draw(self):
        for i in range(self.side):
            print("* " * self.side)


square = Square(10)
square.draw()
print()
