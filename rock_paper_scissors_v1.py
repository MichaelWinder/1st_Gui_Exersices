import random
import easygui
weapons = ["Rock", "Paper", "Scissors"]
pscore = 0
cscore = 0
reply = easygui.ynbox("Welcome to Rock-Paper-Scissors\nRock beats "
                      "Scissors\nPaper beats Rock\nScissors Beats Paper\n\n"
                      "Do you want to play?", "Welcome and Rules")
while reply:
    winner = ""
    weapon = easygui.buttonbox("Choose your Weapon Scum", "Choose "
                               "Weapon", choices=weapons)
    computer_choice = random.choice(weapons)
    if weapon == computer_choice:
        easygui.msgbox(f"It's a Draw!\nYou picked {weapon} and the Computer "
                       f"picked {computer_choice}\nThe score is\nYou: "
                       f"{pscore}\nComputer:{cscore}")
    elif weapon == "Paper" and computer_choice == "Rock":
        winner = "Player"
    elif weapon == "Scissors" and computer_choice == "Paper":
        winner = "Player"
    elif weapon == "Rock" and computer_choice == "Scissors":
        winner = "Player"
    elif weapon == "Paper" and computer_choice == "Scissors":
        winner = "Computer"
    elif weapon == "Rock" and computer_choice == "Paper":
        winner = "Computer"
    elif weapon == "Scissors" and computer_choice == "Rock":
        winner = "Computer"
    if winner == "Player":
        pscore += 1
        easygui.msgbox(f"You Win!\nYou picked {weapon} and the Computer "
                       f"picked {computer_choice}\nThe score is\nYou: "
                       f"{pscore}\nComputer:{cscore}")
    elif winner == "Computer":
        cscore += 1
        easygui.msgbox(f"YOU LOSE! HAHA!\nYou picked {weapon} and the Computer"
                       f" picked {computer_choice}\nThe score is\nYou: "
                       f"{pscore}\nComputer:{cscore}")
easygui.msgbox(f"The Final score is\nYou: {pscore}\nComputer:{cscore}")
quit()
