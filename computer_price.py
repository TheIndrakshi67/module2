class Computer:
    __max_price=900
    def __init__(self):
        pass
    def sell(self):
        print(Computer.__max_price)
    def setmaxprice(self,price):
        Computer.__max_price=price
com=Computer()
com.sell()
com.setmaxprice(1000)
com.sell()