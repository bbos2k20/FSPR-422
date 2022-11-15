# bool
# True , False / 1 , 0 
# любое число что не ноль = это правда (True)
# если переменная пустаю = то она ложь (False)

# x = 12
# y = 41

# if x < y:
#     print(True)
# else :
#     print(False)


"name, surname".split() # ['name' , ' surname']
# a if condition else b
# print(True if x < y else False)
# == ,!= , >=, <=,<, is, is not, in , not in , not, and, or
# []{} "" 0
# if {} :
#     print(True)
# if 0 : 
#     print(True)
# if -13 : 
#     print(True)

name = 'abbos'
surname = 'Jaloliddinov'
age = 20
# # даже если пропустить пробел то выйдет else
# if name == 'abbos' and age == 20:
#     print(name,age)
# else :
#     print('error')

# if name == 'abbos' or age == 20:
#     print(name,age)
# else :
#     print('OR')



if age:
    print(age)
else:
    print('age is false')




# if not age:
#     print(age)
# else:
#     print('age is false')


# if (name == "abbos" and age >= 20 ) or surname == "Jaloliddinov" :
#     print(name,surname, age)
# else:
#     print ("Invalid name,age,surname")


# # is, ==
# #is сравнивает id  2 разных значений
# # id()
# a= 1
# b= 1
# print(id(a), id(b))

# t_1 =()
# t_2 =()
# print(t_1 is  t_2)
# print( id(t_1), id(t_2))
# print("1==1", 1==1,1 is 1)


# l_1 = [1]
# l_2 = [1]
# print(id(l_1), id(l_2)) # id разное так как список можно изменить


# a_1 = [1,2,3]
# a_2 = [1,2,3]
# print(a_1 == a_2)
# print(a_1 is a_2)



# d_1 = {1: 1}
# d_2 = {1: 1}
# print( "dict" , d_1 == d_2) # сравнивает значения 
# print( "dict" , d_1 is d_2) # сравнивает id 


# isinstance - показывает какого типа тип



# name = "ABBOS"
# print(isinstance(name, int)) # Flase
# print(isinstance(name, str)) # True

argument = str(input('ВВЕДИТЕ что то :'))
if argument == str:
    print("это str")
elif argument == int:
    print("это int")











# in = в
# print( 1 in [2,3,4,5,1]) # True


# print( "hi " in "hi, my name is abbos") # True
# print( "hi " in "Hi, my name is abbos") # False буквы не совподают 



# print ([1,2,3] in [1,2,3,4,5,[1,2,3]])
