n=int(input("Enter a number: "))

if n%20==0:
    print("twist")
elif n%15==0:
    pass
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("fizz")
else:
    print("not divisible")