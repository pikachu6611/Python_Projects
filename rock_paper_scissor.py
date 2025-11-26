"""rock vs paper => paper wins
rock vs scissor => rock wins
paper vs scissor => scissor wins
"""

import random

l = ['rock', 'paper', 'scissor']

while True:
    ccount = 0
    ucount = 0
    uc=input("""
    Do you want to play?
    Press 1 for "Yes"
    Press 2 for "No
    """
)
    if uc=="1":
        for a in range (1, 6):
            userInput = int(input("""
1. Rock
2. Paper
3. Scissor

Select 1, 2, or 3
            """))
            if userInput==1:
                uChoice="rock"
            elif userInput==2:
                uChoice="paper"
            elif userInput==3:
                uChoice="scissor"
            else:
                print("Invalid choice")
            C_choice = random.choice(l)
            print("Your choice: ", uChoice)
            print("Computer choice: ", C_choice)
            if uChoice==C_choice:
                print("This round draw")
                ccount += 1
                ucount += 1
            elif uChoice=="paper" and C_choice=="rock"  or uChoice=="rock" and C_choice=="scissor" or uChoice=="scissor" and C_choice=="paper":
                print("You win this round")
                ucount += 1
            else:
                print("Computer won this round")
                ccount += 1

        if ucount == ccount:
            print(f"\nMatch Draw.\nFinal score: You {ucount}. Computer {ccount}")
        elif ucount > ccount:
            print(f"\nYou won.\nFinal score: You {ucount}. Computer {ccount}")
        else:
            print(f"\nComputer won.\nFinal score: You {ucount}. Computer {ccount}")

    else:
        break
