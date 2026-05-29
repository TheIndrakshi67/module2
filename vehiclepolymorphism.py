class Ferrari:
    def fueltype(self):
        print("Ferrari fuel type is petrol")
    def maxspeed(self):
        print("ferrai max speed is 340km/hr")
class BMW:
    def fueltype(self):
        print("BMW fuel type is petrol")
    def maxspeed(self):
        print("BMW max speed is 250km/hr")

cars=[Ferrari(),BMW()]
for car in cars:
    car.fueltype()
    car.maxspeed()
    