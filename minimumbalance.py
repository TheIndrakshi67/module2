balance=5000
try:
    amount=int(input("Enter amount to be widrawn: "))
    if amount>balance:
        raise Exception("insufficient balance")
except Exception as e:
    print(e)