import random


start = "y"

score = 0
com_score = 0

while start == "y":
    user = input("กรุณาเลือก: rock, paper หรือ scissors: ").lower().strip()

    computer = random.choice(["rock", "paper", "scissors"])

    if user not in ["rock", "paper", "scissors"]:
        print("กรุณาเลือก rock, paper หรือ scissors เท่านั้น")
        continue
    if user == "rock" and computer == "scissors":
        print("You win! | computer choose " + computer)
        score += 1
    elif user == "scissors" and computer == "paper":
        print("You win! | computer choose " + computer)
        score += 1
    elif user == "paper" and computer == "rock":
        print("You win! | computer choose " + computer)
        score += 1
    elif user == computer:
        print("Draw! | computer choose " + computer)
    else:
        print("You lose! | computer choose " + computer)
        com_score += 1
    
    print("Your score: " + str(score) + " | Computer score: " + str(com_score))
    print("Do you want to play again? (y/n)")
    start = input().lower()
