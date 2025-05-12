import random


start = "y"

score = 0
com_score = 0

item = ["rock", "paper", "scissors"]

def display_message(result, computer):
    if result == "win":
        print("You win! | computer choose " + computer)
    elif result == "lose":
        print("You lose! | computer choose " + computer)
    else:
        print("Draw! | computer choose " + computer)
        
while start == "y":
    user = input("กรุณาเลือก: rock, paper หรือ scissors: ").lower().strip()

    computer = random.choice(item)

    if user not in item:
        print("กรุณาเลือก rock, paper หรือ scissors เท่านั้น")
        continue
    if user == "rock" and computer == "scissors":
        display_message("win", computer)
        score += 1
    elif user == "scissors" and computer == "paper":
        display_message("win", computer)
        score += 1
    elif user == "paper" and computer == "rock":
        display_message("win", computer)
        score += 1
    elif user == computer:
        display_message("draw", computer)
    else:
        display_message("lose", computer)
        com_score += 1
    
    print("Your score: " + str(score) + " | Computer score: " + str(com_score))
    print("Do you want to play again? (y/n)")
    start = input().lower()
