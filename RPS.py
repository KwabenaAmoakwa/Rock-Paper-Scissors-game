import random

user1 = input("\nPick any option between 'rock','paper' and 'scissors' to begin: ")

user1.lower()
rpy = ['paper','rock','scissors']
cpu = random.randint(0,2)
userind = 0
stat = 0

for i in rpy:
    if user1==i:
        userind = rpy.index(i)
        
        print(f"\nComputer chose : {rpy[cpu]}\n")

        if cpu == userind:
            print("It's a tie")
        elif cpu - userind == -1 or cpu - userind == 2:
            print("Computer won")
        else:
            print("You won")
        stat = 1
        
if stat == 0:
    print("invalid input")




