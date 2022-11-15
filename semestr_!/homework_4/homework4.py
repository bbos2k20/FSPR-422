



A = {'a', 'c', 'd'}
B = {'c', 'd', 2213 }
C = {1, 23, 324}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))

print('A.union() =', A.union())






A = {1, 3, 5}
B = {2, 4, 6}
C = {0}

print('Original A:', A)

A.update(B, C)

print('A after update()', A)





print("=========================================================================================")


A = {'a', 'b', 'c', 'd'}
removed_item = A.pop()
print(removed_item)





numbers = {1,2,3,4,5,6}
numbers.add('abc')
print(numbers)




numberss = {1,2,3,4,5,6,7,123123123}
numberss.remove(123123123)
print(numberss)







names = {'abbos','xumo','jam'}
new_name = names.copy()
print('old names', names)
print('new copied names', new_name)






lists = {'hello',1,2,3,4}
lists.clear()
print(lists)



dictionary = {
    "name" : "abbos",
    "age": 18,
    "from": "uzb"
}

dictionary = dictionary.items()
print(dictionary)



dictionary_1 = {
    "name" : "abbos",
    "age": 18,
    "from": "uzb"
}
dictionary_1 = dictionary_1.values()
print(dictionary_1)