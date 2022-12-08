numbers = []
for i in range(10):
    numbers.append(i)

# print(numbers)

# Comprehension
numbers = [i + 1 for i in range(10)]
print(numbers)

numbers = [i + 1 for i in range(10) if i >= 5]
print(numbers)


numbers = [i + 1 if i >= 5 else False for i in range(10)]
print(numbers)
