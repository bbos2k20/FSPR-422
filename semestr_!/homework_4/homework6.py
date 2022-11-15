for val in [1, 2, 3, 4, 5, [6, "Hello",7, 8, 5, 6], (4, 5, 6)]:  
    if isinstance(val, (int)):  
        print(val)

    if isinstance(val, (list, set, tuple)): 
        for i in val: 
            print(i)
       

print("list")
numbers_1 = [1, 2, 3, 4, 5, 6 , 7]
numers_2 = []
for num in numbers_1:
    numers_2.append(num * 4)
print(numers_2)