try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    print (num1/num2)

except ValueError:
    print("Invalid input. ")
except ZeroDivisionError:
    print("You can't divide by zero.")
