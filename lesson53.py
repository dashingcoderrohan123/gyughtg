#Write a program to generate a random integer and match it with the input given by the user?

import random


playing=True
random_number=random.randint(1,10)


while playing:
    r=int(input("enter the number"))
    if r==random_number:
        print("You have win the game")
        print("the random number is",random_number)
        break
    else:
        print("you have the lost game")
