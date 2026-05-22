class Cclass:
    __privateVar=2
    def __privMeth(self):
        print("private method.")
    def hello(self):
        print (self.__privateVar)
        self.__privMeth()

obj=Cclass()
obj.hello()
print(obj.__privateVar)