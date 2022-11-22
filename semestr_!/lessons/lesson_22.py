class Marker:
    size = 15
    health = 10
    def __init__(self,company,color,price):
        self.company = company
        self.color = color
        self.price = price

    # метод класс
    def draw(self,line_lenght):
        while self.health > 0:
            if self.health == 0:
                print("фломастер уже умер")
                break
        self.health -= 1
        self.health -= line_lenght


marker = Marker("Marker inc.","red",18)
marker_2 = Marker("Maker inc.","blue",20)
marker_3 = Marker("Mar inc.","black",8)

print(marker.company)
print(marker.price)
print(marker.color)
print(marker.size)


print(marker_2.company)
print(marker_2.price)
print(marker_2.color)
print(marker_2.size)

print(marker_3.company)
print(marker_3.price)
print(marker_3.color)
print(marker_3.size)


print("health = ",marker.health)
marker.draw(1)
print("health =",marker.health)
marker.draw(5)
print("health =",marker.health)
print(marker.draw(5))
print("health =",marker.health)