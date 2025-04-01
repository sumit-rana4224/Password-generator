import random
a=[1,2,3,4,5,6]
x=2
x=int(input("Enter 1 to start rolling or 0 to exit :  "))
while x :
    print(random.choice(a))
    x=int(input("Enter 1 to re roll or 0 to exit :  "))
print("Thank You")
    