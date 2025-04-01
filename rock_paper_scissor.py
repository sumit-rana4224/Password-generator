import random
print("Game loading.....")
print("Rock Paper Scissor")
a=0
alert=1
player_choice=0
a=int(input("Enter 1 to Start the game or 0 to exit:  "))
while a:
    while alert: 
        player_choice=int(input("Enter 1-Paper 2-Scissor 3-Stone :   \n"))
        if (player_choice != 1 and player_choice != 2 and player_choice != 3):
            print("Enter a valid choice:  ")
        else:
            break
    data=[1,2,3]
    bot_choice=random.choice(data)
    print(bot_choice)
    if(bot_choice==player_choice):
        print("Match Draw!!\n")
    elif(bot_choice==1 and player_choice==2):
        print("You Win!!!\n")     
    elif(bot_choice==3 and player_choice==1):
        print("You Win!!!\n") 
    elif(bot_choice==2 and player_choice==3):
        print("You Win!!!\n")
    else:
        print("You lose @@\n")
    
    a=int(input("Enter 1 to Restart the game or 0 to exit:"))

print("Thank You")