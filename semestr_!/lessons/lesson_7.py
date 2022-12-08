user_date = {
    "ключ": "значение",
    1: None,
    2: 21,
    3: 6.7,
    4: [2, 3, 4],
    5: {"key ": "другой словарь"},
}


# print(user_date[1] ,user_date[2], user_date[3],user_date[4],user_date[5],  sep='\n')

user_data = [
    {
        "username": "gobby",
        "password": "asjdasjdw",
        "age": 14,
    },
    {
        "username": "abbos",
        "password": "wioqdjssjdw",
        "age": 17,
    },
]


print(user_data[0]["age"], user_data[1]["age"])
user_data = {"username": "abbos", "password": "djs;aldj", "age": 12}
user_data["age"] = 18
print(user_data.keys(), user_data.values(), user_data.items(), sep="\n")

user_list = list(user_data.values())
print(user_list)

print("get:", user_data.get("age"), user_data.get("name"))


remove_duplicates = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, "AA", "BB", "AA"]
print(remove_duplicates, set(remove_duplicates), sep="\n")

print(list(set(remove_duplicates)))


list
tuple
set
dict
