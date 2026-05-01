set_int={10,20,30,40}
print("Integer set: ", set_int)
set_mixed={1,"Hello",3.14,True}
print("Mixed set: ", set_mixed)
set_duplicates={1,2,3,4,3,2}
print("Set from duplicates: ", set_duplicates)
my_list=[1,2,3,2]
set_from_list=set(my_list)
print("Set from list: ", set_from_list)
lst=list(set_int)
lst.remove(10)
print(lst)