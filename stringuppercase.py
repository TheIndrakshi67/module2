class IOString:
    def __init__(self):
        self.str1=""
    def get_String(self):
        self.str1=input("Enter a string: ")
    def print_String(self):
        print("upper case string: ", self.str1.upper())
obj=IOString()
obj.get_String()
obj.print_String()