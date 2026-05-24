class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare
capacity_input = int(input("Enter the seating capacity of the bus: "))
my_bus = Bus(capacity_input)
final_fare = my_bus.fare()
print(final_fare)
