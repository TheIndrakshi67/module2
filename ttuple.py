
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)


def calculate_product(t):
    result = 1
    for num in t:
        result *= num
    return result


print("Product of tup1:", calculate_product(tup1))
print("Product of tup2:", calculate_product(tup2))
