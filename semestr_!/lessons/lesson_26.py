# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()






class Сustomer:
    def __init__(self,name ,email,password,card):
        self.name = name
        self.email = email
        self.password = password
        self.card = card
#       получение имени пользователя 

    def get_name(self):
        self.name = input("write ur name: ")
        for i in self.name:
            if i.isdigit():
                raise ValueError("Имя не должно содержать цифр!")

 #      получение email пользователя 
   
    def get_email(self):
        self.email= input("Write ur email with '@' !: ")
        if "@" in self.email:
            print ("данные получены!")
        else :
            return print("ARE u stupid?")

#      получение пароля пользователя 

    def get_passwor(self):
        self.password = input("Введите пароль: ")
        if len(self.password) < 6:
            print ("минимальное колличество символов 6! ")
        else:
            print ("пароль сохранён! ")


#      получение пластик карты пользователя 

    def get_card(self):
        self.card = input("Введите пластик карту: ")
        if len(self.card) == 16 :
            print("Всё верно")
        else:
            print("что то не так. проверьте всё ли верно написали!")



# class User:
#     def check_name():
#         name_checking =""
#         if name_checking = 
pr1=Сustomer(2,2,2,2)
print(pr1.get_name())
print(pr1.get_email())
print(pr1.get_passwor())
print(pr1.get_card())