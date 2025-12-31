# Rock-Paper-Scissor-game.py
"""

workflow of project:

1_ input from user(Rock,Paper,Scissor)
2_ computer  choice(computer will choose randomly not condition) 
3_ result print

cases:
A - Rock  
Rock -Rock = tie
Rock - paper =  paper win
Rock -scissor = Rock win

B- paper
paper - paper = tie
paper - Rock = paper win
paper - scissor= scissor win


 C- scissor
 scissor -  scissor = tie
 scissor - Rock = Rock win
 scissor - paper =  scissor win

"""
import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice  == comp_choice:

   print("Both chooses same : =  Match Tie ")

elif  user_choice ==" Rock":
   if comp_choice == "Paper":
        
    print('Paper covers Rock = Computer')
   else:
    print("Rock smesh Scissor =You win")
elif  user_choice =="Paper" : 
  if  comp_choice == "Scissor":
       print("Scissor cuts  paper ,computer win")
  else:
       print("Paper covers rock , you win")


elif user_choice == "Scissor":
       if comp_choice == "Paper":
             print("Scissor cuts paper, you win")
       else :
           print("Rock smashes scissor,computer win")       
