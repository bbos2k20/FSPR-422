def name_surname(name,surname,last_name = "отчество"):
    # code
    return name,surname, last_name

result = name_surname("abbos","jaloliddinov")
print(result) 


# правило передачи аргументов

def order_of_args(name,default,*args,sep="seperator",username,end = "\n",**kwargs):
    print(name,default,args,sep, username ,end,kwargs)

order_of_args("abbos",123,4,5,6, username="wsflo",end="not enter",email="dwfq@mail.ru",loot=[2,3])




def some(*args,**kwags):
    print(args,kwags)

some(2,3,4,5,[6],user={"name":"ya"},goal=("win chempionship"))