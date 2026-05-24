from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self,amount):
        self.amount=amount
    def amttopay(self):
        print(self.amount)
    @abstractmethod
    def processpayment(self):
        pass

class Credit_card(Payment):
    def processpayment(self):
        print(self.amount)
class UPI(Payment):
    def processpayment(self):
        print(self.amount)
    
person1=Credit_card(200)
person1.amttopay()
person1.processpayment()

person2=UPI(100)
person2.amttopay()
person2.processpayment()
