import random
data= random.randint(1,100)
user=int(input("Enter A number between 1 to 100: "))
count =1
while(data!=user):
    if data>user:
        user=int(input("Enter a big number: "))
        count+=1
    else:
        user=int(input("Enter a small number: "))
        count+=1
print("Number founded successfully in ",count,"attempt")