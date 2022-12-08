# a = [1,2,3,4,[2,3]]
# b = a.copy()
# b[2] = 400
# b[4][1] = 12
# print('a=',a,'b=', b)


# # импорт глобокого копирования

# import copy


# a = [1,2,3,4,[2,3]]
# b = copy.deepcopy(a)
# b[2] = 400
# b[4][1] = 12
# print('a=',a,'b=', b)


# # дз 1
# print (type("qwerty"), str,"qwert" == str)

# val = input("Введите что то: ")
# if type(val) == int or type(val) == str:
#     print(True)
# else:
#     print(False)


print("list")

numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    print(num + 2)


print("tuple")

numbers = (1, 2, 3, 4, 5, 6, 7)
for num in numbers:
    print(num + 2)


print("set")

numbers = {1, 2, 3, 4, 5, 6, 7}
for num in numbers:
    print(num + 2)


print("dict ")
user = {
    "name": "abbos",
    "age": 17,
    "skill": "swim",
}
for key in user:
    print(key)

print("dict vals")
for val in user.values():
    print(val)


print("\ndict items")
for key, val in user.items():
    print("key =", key, "val =", val)
