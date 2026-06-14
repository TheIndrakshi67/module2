# Create a class as required by the project
class RomanConverter:
    def int_to_roman(self, num):
        roman_num = ""
        
        # Check each Roman numeral from largest to smallest
        while num >= 1000:
            roman_num += "M"
            num -= 1000
            
        while num >= 900:
            roman_num += "CM"
            num -= 900
            
        while num >= 500:
            roman_num += "D"
            num -= 500
            
        while num >= 400:
            roman_num += "CD"
            num -= 400
            
        while num >= 100:
            roman_num += "C"
            num -= 100
            
        while num >= 90:
            roman_num += "XC"
            num -= 90
            
        while num >= 50:
            roman_num += "L"
            num -= 50
            
        while num >= 40:
            roman_num += "XL"
            num -= 40
            
        while num >= 10:
            roman_num += "X"
            num -= 10
            
        while num >= 9:
            roman_num += "IX"
            num -= 9
            
        while num >= 5:
            roman_num += "V"
            num -= 5
            
        while num >= 4:
            roman_num += "IV"
            num -= 4
            
        while num >= 1:
            roman_num += "I"
            num -= 1
            
        return roman_num

# Ask the user for a number
user_input = int(input("Enter a number: "))

# Create the object
converter = RomanConverter()

# Call the method and print the answer
result = converter.int_to_roman(user_input)
print("Roman numeral:", result)
