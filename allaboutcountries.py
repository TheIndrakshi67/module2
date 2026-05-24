class Japan():
    def capital(self):
        print("Tokyo")
    def language(self):
        print("Japanese")
    def currency(self):
        print("¥ (yen)")
class India():
    def capital(self):
        print("Delhi")
    def language(self):
        print("Most spoken: Hindi")
    def currency(self):
        print("Rupees")

jpn=Japan()
ind=India()

for country in (jpn, ind):
    country.capital()
    country.language()
    country.currency()
    
