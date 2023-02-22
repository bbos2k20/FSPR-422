import csv  
with open("csv_file.csv", 'w', newline = '') as file: 
    writer = csv.writer(file) 
 
    writer.writerow(['No', 'Player', 'Record']) 
    writer.writerow([1, 'Ogabek', '433']) 
    writer.writerow([2, 'Damn', '345']) 
    writer.writerow([3, 'Pro Player', '563']) 
    writer.writerow([4, 'Player_2', '576']) 
    file.close()
w=3
while True:
    age=  input("возраст: ")
    name=input("имя: ")
    surname=input("Фамилия: ")
    passport=input("Паспорт: ")
    mail =input("мэил: ")
    if "@"  in mail:
        print("прошли проверку")
    elif w==1:
        print("поставьте @")
        break
    else:
        print("поставьте @!!!!!!!")
        w-=1
    



list = [age,name,surname,passport,mail]
Names= ['abbos','ogabek','behruz']
with open('csv_file.csv','a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(list)
    file.close()