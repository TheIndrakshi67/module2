def calculate_due_amount(bill, paid):

    change = paid - bill

    return change


total_bill = 2.50
amount_paid = 4.00


due_amount = calculate_due_amount(total_bill, amount_paid)


print(f"The shopkeeper should return: ${due_amount:.2f}")
