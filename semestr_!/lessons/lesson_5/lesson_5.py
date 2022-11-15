"""
изменяемые

list -список
dict- словарь
set - множества 

неизменяемы 

frozenset- множество
typle- кортеж
bin - 

"""
"kasldsjfsl"

# names= []
# print(names)
# names = list()
# print(names)

# #        0 1 2 3  4 5 6    7   8       9   10
# names = [1,2,3,45,6,7,12.4,6,'Abcd',True,None]
# print(names)
# names[0] = False
# print(names)
# # names[7] = "name"

# print(names[8][0])  #abcd -> a

# #

# names= [[2, 3 ,4 ],[2.3, 4.5 , 33.4],['go','go1','go2' ]]

# print(names[2][2])

# slice- сласы- нарезки
# миерировать - прохожиться по элементам итеррируемых переменнвх (эти такие переменные, которые могут хранит больше одного значения)


numbers = [4, 3, 54,22, 2.4,324,3322,2]
# print(numbers[1:5])
# print(numbers[:], numbers )
# print(numbers[1: ])
# print(numbers[:5])


print(numbers[:6:2])
print(numbers[:6])
print(numbers[::2])
print(numbers[::10])


name = ('qwerty'[::])
print(name)