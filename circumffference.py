import math

def calculate_circumference(radius):
    """
    Returns the circumference for a given radius.
    Formula: 2 * pi * r
    """
    return 2 * math.pi * radius


user_input = input("Enter the radius of the circle: ")
radius = float(user_input)


result = calculate_circumference(radius)

print(f"For a radius of {radius}, the circumference is: {result:.2f}")

