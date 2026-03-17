lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
for num in range(lower, upper+1):
    if num>1:
        for j in range(2, num):
            if num%j==0:
                break
        else:
            print(num,end=" ")