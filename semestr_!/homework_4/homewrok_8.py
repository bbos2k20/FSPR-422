n = 7
treeHeight = int(n / 2) + 1 
trunkHeight = int(treeHeight/2)
for i in range(treeHeight):
    print(' ' * int(n / 2 - i), '*' * (1 + i * 2), ' ' * int(n / 2 - i))
for y in range(trunkHeight):
    print(' ' * int(n / 2), '*', ' ' * int(n / 2))



# 2 dz

numbers = [2, 3, 4, 5, 6]
even = []
uneven = []
for i in numbers:
    residue = (i % 2) 
    if (residue == 0):
        even.append(i)
    else: 
        uneven.append(i)
print("четные - ",  *even, sep=' ')
print("нечетные - ",  *uneven, sep=' ')

# 3 dz

faranheitsList = [20, 19, 24, 45] 
celsiusList = []
i = 0
while i < len(faranheitsList):
    celsius = ((faranheitsList[i] - 32) * 5 / 9)
    celsiusList.append(celsius)
    i += 1
    if celsius > 50:
        print("Слишком горячо")
        break
    elif celsius < 5:
        print("Жить можно")
        continue
    print(f"На улице {celsius} по цельсию")

# 4 dz

square_line = 4 
star = "*" 
star_width = star * square_line  
i = 0
while i < square_line:
    if i > 0 and i < (square_line - 1): 
        empty_space = " " * (square_line - 2) # 4 "  "
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)
    i += 1