faranheits = [20, 19, 24, 45]

for faran in faranheits:
    celsius = (faran - 32) * 5 / 9
    if celsius >= 50:
        print("ЖАРААА")
        continue
    elif celsius <= 5:
        print('очень холодно')
    else:
        print("жить можно")
    print("celsius =", celsius, "faranheit =", faran)




info = []

for x in range(10):
    age = input(str("Введите свой возраст: "))
    name = input("Введите свой имя: ")

    info.append({ "age": age, "name": name })

print(*info, sep="\n")