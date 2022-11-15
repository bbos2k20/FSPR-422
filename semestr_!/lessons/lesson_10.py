# a, b, *_ = (2,3,3,4,5,6)
# print(a,b,_)

# for i in range(10):
#     print(i)



# print("Next range")

# for i in range(4,10):
#     print(i)




# print("Next range")

# for i in range(4,10, 2):
#     print(i)




numbers = [1,2,3,4,5,6,7,5]
for val in numbers:
    if val == 5 or val== 7 or val ==4:
        print(f"пропустить{val}")
        continue
    print("val= ", val)



numbers = [1,2,3,4,5,6,7,5]
for val in numbers:
    if val == 5 or val== 7 or val ==4:
        print(f"выйти из цикла")
        break
    print("val= ", val)

if 1 == 1:
    pass

