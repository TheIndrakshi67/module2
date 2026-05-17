class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
user_input = input("Enter the radius: ")
user_radius = float(user_input)
my_circle = Circle(user_radius)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
