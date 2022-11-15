def shades_of_grey(n):
    shades = []
    hex ='123456789abcdef'
    counter = 0
    for i in range(n):
        if counter ==15:
            counter = 0
        gray =f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
        if i >= 15:
            gray = f'#1{hex[counter]}1{hex[counter]}1{hex[counter]}'
        shades.append(gray)
        counter += 1

    return shades
print(shades_of_grey(50))


def logic(n, num):
    numbers = []
    for i in range(n):
        numbers.append(i * num)
    return numbers

print(logic(20, 3))
print(logic(10, 4))





def func(a, b, default="hi"):
    print(a, default)

# func(12)
# func(12, "not hi")

def func(a, b, default="hi"):
    print("a =", a, "b =", b, default)

# func(12, 4)
# func(b=12, a=4)
# func(12, 5, "not hi")

# арги
def func(a, b, default="hi", *args):
    print(a, b, "default =", default, "args =", args )

# func(12,4, "yeeeeeey,3,4,[2,3,4")

def any_args(*args):
    """Функция которая принимат любое колличество аргументов и выводит их на экран"""
    print("args=", args)
    for arg in args:
        print(arg)
any_args(2,3,4,"goooo","noooooo",{1:1},[],{3,4,5})
any_args()