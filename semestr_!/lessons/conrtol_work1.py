"""
1. Назовате все типы переменных и их особенности
2. Какие типы переменных можно хранить в качестве значений множества и ключа словаря
3. Что такое MRO и наследование в питоне
4. Опишите процесс публикования изменений в гитхаб
5. в чем разница между функцией и методом?

"""

# Теория

# 1

"""
    Изменяемые 

list - список []
set - множество {}
dict - словарь {}
 
    Неизменяемые 

tuple - кортеж ()
None - ничего 
float - дробное число (флоат)
int - число 
bool - True , Flase (правда \ложь)
str - строка 
frozenset - множество 

"""


# 2

"""
Ключом может являться в принципе любой неизменяемый тип данных,
значением же конкретного ключа может быть что угодно ( даже цифры )

И ещё одна деталь  :
если вы попробуете использовать изменяемый тип данных в качестве ключа, то получите ошибку

"""

# 3
"""
Порядок разрешения методов (Method Resolution Order — MRO)

class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1


class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
    def dec(self):
        pass

"""


# 4

"""
git status - проверяем есть ли изменения в коде
git add . - (либо имя файла . либо просто точка ".")
git commit -m "(тут пишем наш коммит)" - делаем киммит
git push - опубликовываем наши изменения 

"""

# 5

"""
Метод это функция класса
Метод всегда является функцией, a функция не всегда является методом


"""


# Теория + Задачи

# 1
"""
    сравнение :
< , > , == , <= , >= , !=

3<4
4==4

    догические :

and = Возвращает True, если оба выражения равны True
or = Возвращает True, если 1 из выражения равно True
not =  Возвращает True, если выражение равно False

    особые :

    Операторы тождественности

is - Возвращает true если переменные являются одним объектом
is not - Возвращает true если переменные разные

    Операторы принадлежности

in - Возвращает True если последовательность присутствует в объекте
not in - Возвращает True если последовательность не присутствует в объекте
"""


# 2

"""
Если говорить кратко, полиморфизм — это способность обьекта использовать методы производного класса, 
который не существует на момент создания базового.
Полиморфизм — одна из 3 основных парадигм ООП. 

"""


# 3


def validate(username, password):
    if username == "Random" and password == "2321ewfsef":
        return "Вы успешно вошли в систему!"
    else:
        return "Пароль или имя пользователя не правильн"


def check():

    print(validate("Random", "2321ewfsef"))


print(check)


# 4
"""
Локальная
Глобальная
Нелокальная


# global
def parent():
    # enclosed
    a =5 
    def sui():
        # local
        return a
    return sui()

print(parent())

"""


# 5
"функция 'рекурсия'- функция вызывающаяя сама себя "


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(15))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")







# Задачи

def get_data(code = 1, salary = "fhdsuhf", *args, **kwargs): 
    other_info = [code, salary, *args] 
    for arg in args: 
        print(arg) 
    for key, val in kwargs: 
        get_data((key, val)) 
 
    return other_info
print(get_data())



