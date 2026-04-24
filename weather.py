weather1=(20,23,22,23,21,19,19)
average=sum(weather1)/len(weather1)
print(average)
if average>31:
    print("It's going to be hot")
else:
    print("Its not hot.")