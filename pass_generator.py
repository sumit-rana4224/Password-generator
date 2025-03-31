import random
import string
pass_len=int(input("Enter length of password: "))
data  = string.ascii_letters
data +=string.punctuation
data +=string.digits
password=""
while len(password)!=pass_len :
    password +=random.choice(data)

print("Password is :",password)