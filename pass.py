import random
import time

print("This is a password generator..")
time.sleep(1)
length = int(input("Enter the length of the password you need to generate : "))
if length>5:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!@#$%^&*()"

    characters = letters + digits + punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("The password you got : ",password)
else:
    print("Invalid length .. The password must alteast 5 characters length.!")
