class Vehicle:
    def __init__(self, maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
car=Vehicle(180,18)
car2=Vehicle(200,20)
print("Maximum Speed of car 1: ", car.maxspeed)
print("Mileage of car1: ", car.mileage)
print("Maximum Speed of car 2: ", car2.maxspeed)
print("Mileage of car2: ", car2.mileage)