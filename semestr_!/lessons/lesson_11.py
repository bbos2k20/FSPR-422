# square_line = 6
# star = "*"
# star_width = star * square_line
# for i in range (square_line):
#     if i > 0 and i < (square_line - 1):
#         empty_space = " " * (square_line - 2)
#         print(f"{star}{empty_space}{star}")
#     else:
#         print(star * square_line)

    
i = 0
while i < 10:
    print("i= ", i)
    i += 1



i = 0
while True:
    print("i= ", i)
    i += 1
    if i == 100:
        break


names = [1,2,3,4,5,6]
i = 0 
while i < len(names):
    print(names[i])
    i += 1





s = "ABCDEFG"
for i in range(len(s)):
    s[i]

for i, val in enumerate("ABCDEFG"):
    print(i, val)


list_dublicate = [1, 3, 5, 6, 3, 5, 6, 1]
print ("Оригинальный список : " + str(list_dublicate))
list = []
for i in list_dublicate:
  if i not in list:
    list.append(i)
print ("список после удаления дубликатов : " + str(list))






