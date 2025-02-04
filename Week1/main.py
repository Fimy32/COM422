from Week1.car import Car

car1 = Car("Big Car",10,100,0)

car2 = Car("Super Car",5,50,0)

print(car1.currentSpeed,car2.currentSpeed)

car1.race()

car2.race()

print(car1.currentSpeed,car2.currentSpeed)
