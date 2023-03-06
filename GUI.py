import random
import easygui
# name = easygui.enterbox("What is your name? ", "Name")
# age = easygui.integerbox("How old are you? ", "Age")
# option = easygui.buttonbox("Do you want to continue", choices=["Yes", "No"])

# for i in range(100):
#     number = random.randint(0, 5)
#     print(number)

# words = ["bat", "mat", "cat", "hat"]
# my_word = random.choice(words)
# print(my_word)

# word = input("What is your name? ")
# letter = random.choice(word)
# print(f"The random letter chosen in {word} is {letter}")
num = 1
while True:
    elefant_letter = random.choice("elephant")
    easygui.msgbox(f"A random letter is {elefant_letter}", f"Letter {num} "
                                                           f"chosen")
    num = num + 1
