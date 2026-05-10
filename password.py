import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

length = 12
password = ""

for i in range(length):
    random_char = random.choice(chars)
    password = password + random_char


password_list = list(password)
random.shuffle(password_list)


final_password = "".join(password_list)
print("Your new password is:", final_password)
