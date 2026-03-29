num=int(input("Enter a number: "))

def cube (num):
    ans=num**3
    print(ans)
def divisibility (num):
    
    if num%3==0:
        cube(num)
    else:
        print("Number isn't divisible by 3.")
        
divisibility(num)