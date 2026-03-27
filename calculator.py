def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x//y 

print("Choose 1 for addition, 2 for Subtraction, 3 for multiplication and 4 for division")
choice=int(input("Enter choice: "))
num1=int(input("Enter the first number."))
num2=int(input("Enter the second number."))

if choice ==1:
    print(add (num1, num2))

elif choice==2:
    print(subtract(num1, num2))

elif choice==3:
    print(multiply(num1, num2))

elif choice==4:
    print(divide (num1, num2))
else:
    print("invalid choice")
    