try:
    age = int(input("enter your age: "))
    if age % 2 == 0:
        print("the age entered is even.")
    else:
        print("the age entered is odd.")
except ValueError:
    print("Error: Please enter a valid integer for age.")