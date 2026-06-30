#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Welcome To The Game Rock Paper Scissor")

option = ["Rock","Paper","Scissor"]
print("Your Choices:",option)
uin = input("Enter Your Choice: ")
comp = random.choice(option)

print(f"You chose: {uin}")
print(f"Computer chose: {comp}")

# Convert user input to match case (handle case sensitivity)
uin = uin.capitalize()

# Check if input is valid
if uin not in option:
    print("Invalid Input")
else:
    # Tie Case
    if comp == uin:
        print("Game is Tie")
    
    # Computer win cases (fixed logic)
    elif (comp == "Rock" and uin == "Scissor") or \
         (comp == "Paper" and uin == "Rock") or \
         (comp == "Scissor" and uin == "Paper"):
        print("Computer Win")
    
    # User win cases (fixed logic)  
    elif (uin == "Rock" and comp == "Scissor") or \
         (uin == "Paper" and comp == "Rock") or \
         (uin == "Scissor" and comp == "Paper"):
        print("You Win")

