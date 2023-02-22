users={"bbos":"bbos223",
       "masha":"masha222",
       "danya":"danya211"}

x=input("напишите имя:" )
c=input("напишите пароль:" )
def f():
    if x in users and c in users:
        print("вы вошли в систему")
    else:
        print("error")
    return f 
a =f
print(a)