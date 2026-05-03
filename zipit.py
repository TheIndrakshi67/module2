list1=[1,2,3]
list2=["a","b","c"]

zipped_list=list(zip(list1,list2))
print(zipped_list)

zipped_reverse=list(zip(list1,list2[::-1]))
print(zipped_reverse)

stocks=["infosis", "rakuten", "reliance", "tcs"]
shareprice=[1100,2000,2500,1500]
dict={stocks:shareprice for stocks, shareprice in zip(stocks,shareprice)}
print(dict)