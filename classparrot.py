class Parrot:
    species="Bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age
parrot1=Parrot("Blu",10)
parrot2=Parrot("Rii", 15)

print("Name and age of parrot1: ",parrot1.name, parrot1.age)
print("Name and age of parrot2: ",parrot2.name,parrot2.age)