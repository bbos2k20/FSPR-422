
# # 1 способ

# user_name = input('word:')[::-1]
# print(user_name)

# # 2 способ

# r = ("qwerty"[::-1])
# print(r)

# # 3 способ 

# print('phew'[::-1])



def myyunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myyunc)
print(cars)