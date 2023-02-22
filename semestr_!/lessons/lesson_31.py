

class Bankomat:
    def __init__(self,age,name,balance,login,password):
        self.age = age
        self.name= name
        self.balance = balance
        self.login = login
        self.password = password

    def print_age(self):
        return self.age

    def print_name(self):
        return self.name

    def print_deposit(self):
        cash = float(input("Введите суммы для депозита: "))
        money = self.balance + cash
        return money
        

    
    def get_cash(self):
        cash = float(input("Введите суммы для снятия денег: "))                         
        cash_out = self.balance - cash  
        komisiya = cash_out - (cash_out  % 5)                          
        return cash_out ,komisiya                        
                            
    def obmen(self):
        q = input("Выебрите в какую валюту хотите конвертировать из суммов в: 1)доллар 2)евро : ")
        if q == "1":
            print("Суммы конвертируем в доллары США")
            usd = 11340 #USD к сум
            x = input (str("Введите количество сум: "))
            result = (int (x) / usd )
            print (result)
        elif q==2:
            print("Суммы конвертируем в евро")
            eur = 12329 #USD к сум
            x = input (str("Введите количество сум: "))
            result = (int (x) / eur )
            print (result)
        else:
            print("u chose another number: ")

                            
                    
                            
                            
                            
w = Bankomat(18,"abbos",1000,"NBU","7777",)                          
login =  "NBU"
password = "7777"
rin_log = (input("Введите название банка: "))
rpasw= (input("Введите пароль: "))
count = 0


while count <=2:
    if rin_log == login and rpasw == password:
        menu = input("Выберите дейстиве: 1)info ,2)выдать деньги, 3)депозит денег, 4)обен валют , 5)Выход! : ")
        if menu =="1":
            print("INFO PAGE")
            print("вам столько лет: ",w.print_age())
            print("имя: ",w.print_name())

        elif menu == "2":
            print(w.get_cash())
        elif menu == "3":
            print(w.print_deposit())
        elif menu == "4":
            print(w.obmen())
        elif menu == "5":
            print("Выход совершен. вытащите карту")
            break
    else:
        print("Wrong password or loggin")
        count +=1
        print("U are Blocked")