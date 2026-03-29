bill=int(input("Enter the amount of the bill: "))
tip=int(input("Enter the percentage of tip: "))

def total (bill, tip):
    finaloutput= ((tip/100)*bill)+bill
    print(finaloutput)
total(bill, tip)
