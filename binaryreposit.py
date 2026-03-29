
decimal_num = int(input("Enter a decimal number: "))


binary_result = ""


if decimal_num == 0:
    binary_result = "0"
else:
    temp_num = decimal_num 
    
    
    while temp_num > 0:
        remainder = temp_num % 2           
        binary_result = str(remainder) + binary_result  
        temp_num = temp_num // 2          

print(f"The binary representation of {decimal_num} is {binary_result}")
