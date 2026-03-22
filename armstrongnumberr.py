lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))

num=lower
while num<=upper:
    temp=num
    digit=0
    #count number of digits
    while temp>0:
        digit+=1
        temp//=10
    temp=num
    sum=0




    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
if sum==num:
    print(num)
num+=1