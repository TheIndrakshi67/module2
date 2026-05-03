list1=[1,2,3]
list2=[4,5,6]

def add(x,y):
    return x+y

result=map(add,list1,list2)
print(list(result))

list3=[1,2,3,4,5]

def square(x):
    return x*x

squareresult=map(square, list3)
print(list(squareresult))