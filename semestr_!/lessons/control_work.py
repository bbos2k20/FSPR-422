#1
"""
Роль PVM заключается в преобразовании инструкций байт-кода 
в машинный код, чтобы компьютер мог выполнять эти инструкции машинного кода и отображать результат
"""

"---------------------------------------------------------------------------------------------------------------------------"
#2
"""
int- целые число
str -строка 
float - дробное число
операторы - (+,//,/,%,*,**)
bool -True/False

"""

"-----------------------------------------------------------------------------------------------------------------------------"

#3

"""
не изменяемые
int
float
str
tuple


изменяемые 

list
dict

"""

"-----------------------------------------------------------------------------------------------------------------------------"

#4


# name='Mirabbos'
# surname='Jaloliddinov'
# age=17
# a='меня зовут {},моя фамилия {},и мне {} '.format(name,surname,age) 
# print(a)
# a='меня зовут {1},моя фамилия {0},и мне {2} '.format(name,surname,age) 
# print(a)
# a=f'меня зовут {name},моя фамилия {surname},и мне {age} '
# print(a)
# a=f'меня зовут {name:<10},моя фамилия {surname:<10},и мне {age:<10} '
# print(a)


# 5
"""
проверяет наличие элемента в последовательности.
Выражение x in s принимает значение True, если x является членом s, и False в противном случа:
x =[1, 2, 3, 4, 5, 6, 7, 8]
5 in x -> true

---------------------------------------------------------------------------------------------------

is проверяет идентичность самих объектов. 
Его используют, чтобы удостовериться, что переменные указывают на один и тот же объект в памяти

(проверяет id каждого значения в переменной )
"""

#6
# # global
# def parent():
#     # enclosed
#     a =5 
#     def sui():
#         # local
#         return a
#     return sui()

# print(parent())


#7


"Если в ней нет return , то она возвращает None"



#ЗАДАЧИ

#1 

# def stroka(qwerty):
#     number = len(qwerty[0])
#     lin = ""
#     for j in qwerty:
#         if (len(j) <= number):
#             lin = len(j)
#             lin = j
#     print(lin, " - ", number)
#     return number
            
# qwerty = ["привет", "пока", "здравствуйте "]
# print(stroka(qwerty))


#4

# names = [] 
# for i in range(10): 
#     names.append(i+4) 
#     if i == 7: 
#         names.pop(0) 
# print(names)


#3
string1= "You've got that fire (fire). The flavor, the style (style)"

list1=list(string1.split())

print(list1)
