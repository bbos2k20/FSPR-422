# 1

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(15))

#2


names = []
names_dictionary = {}

names_count = int(input("Введите количетсво имен: "))
for i in range(names_count):
    names.append(input("Введите имя: "))

def to_dictionary(names):
    for i in range(names_count):
        names_dictionary.update({names[i]: None})
    return names_dictionary

print(to_dictionary(names))
a = to_dictionary(names)
print(a)



# 5
# "py -m pip install numpy" - в консоль

import numpy as np 

def matrix(number):
    if number%3 == 0:
        array = np.arange(number).reshape(int(number/3), 3)
    print(array)
        
matrix(12)




