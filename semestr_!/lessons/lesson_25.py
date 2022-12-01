
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    # def __str__(self):
    #     return f"Class info: name{self.name} age= {self.age}"

    def __repr__(self):
        return f"Class info: name{self.name} age= {self.age}"

person = Person("Abbos", 17)
person_2 =Person("xumo", 12)
print(person)