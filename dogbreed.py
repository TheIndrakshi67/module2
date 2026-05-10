class Dog:
    animal="mammal"

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
dog1=Dog("Chihuahua", "Rex")
dog2=Dog("Pug", "Rox")

print("Dog1's name and breed is: ",dog1.breed,dog1.name)
print("Dog2's name and breed is: ",dog2.breed,dog2.name)
