#Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer
import random
options=["rock","paper","scissor"]
string=input("Choose Rock, Paper, or Scissors:")
computer_choice=random.choice(options)
print("You choosed :",string)
print("computer choosed:",computer_choice)
if string==computer_choice:
    print("it is a tie")
elif  string=="rock" and computer_choice=="scissor":
    print("Scissor will smash!!!")   

