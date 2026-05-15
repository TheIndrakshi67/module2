class Employee:
    def __init__(self):
        print("Employee object created")
    def __del__(self):
        print("Employee object deleted.")

obj=Employee()
del obj

