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

    def get_name():
        reg_name = input("write ur name: ")
        for i in reg_name:
            if i.isdigit():
                raise ValueError("Имя не должно содержать цифр!")
    
   
   
    def get_email():
        check_mail= input("Write ur email with '@' !: ")[6:]
        if "@" in check_mail:
            print ("данные получены!")
        else :
            print("ARE u stupid?")
    # print(get_email)
    # get_email()

    def get_passwor():
        password = input("Write ur passwor: ")[6:]
        # if password <= len(password):
            # print("WRONG!!")
    print(get_passwor)
    get_passwor

   
