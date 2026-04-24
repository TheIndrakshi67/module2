tuple1=(("Hello", 10,3.14,True))
tuple2=(1,2,3,2,5,6,7)
tuple3=tuple2+(9,)
for i in range(len(tuple3)):
    print(tuple3[i])
print(tuple2.count(2))
slicing_of_tuple=tuple2[0:3]
print(tuple1)
print(tuple2)
print(tuple3)
print(slicing_of_tuple)