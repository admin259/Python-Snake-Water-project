'''

1 for snake
-1 for water
0 for gun

'''

import random
computer = random.choice([-1, 0, 1])
yourstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1:"Water", 0: "Gun"}

you = youDict[yourstr]

# by now we have two numbers (variables), you and computer
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw!")

if ((computer - you) ==  -2 or (computer - you) == 1):
    print("you win!")
else:
    print("you lose!")


# else:
#     if (computer == -1 and you == 1): = -2
#         print("you win!")
#     elif(computer == -1 and you == 0): = -1
#         print("you lose!") 
#     elif (computer == 1 and you == -1): = 2
#         print("you lose!")
#     elif(computer == 1 and you == 0): = 1
#         print("you win!")
#     elif (computer == 0 and you == 1): = -1
#         print("you lose!")
#     elif(computer == 0 and you == -1): = 1
#         print("you win!")

# this logic is written on the basis of value of computer - you
    