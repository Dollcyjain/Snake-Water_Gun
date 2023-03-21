import random


def game():
    computer = 0
    you = 0
    print(">>> S for snake, W for water, G for gun")
    i = 0
    myActs = ["s", "w", "g"]
    while i < 10:
        myAct = random.choice(myActs)
        act = input("Your action: ")
        if myAct == act:
            computer += 0
            you += 0
            print("Computer action:", myAct)
            print("No Points!!\n")
        elif myAct == "s" and act == "w":
            computer += 1
            print("Computer action:", myAct)
            print("Point for computer\n")
        elif act == "s" and myAct == "w":
            you += 1
            print("Computer action:", myAct)
            print("Point for you\n")
        elif myAct == "g" and act == "s":
            computer += 1
            print("Point for computer\n")
            print("Computer action:", myAct)
        elif act == "g" and myAct == "s":
            you += 1
            print("Computer action:", myAct)
            print("Point for you\n")
        elif myAct == "w" and act == "g":
            computer += 1
            print("Computer action:", myAct)
            print("Point for computer\n")
        elif act == "w" and myAct == "g":
            you += 1
            print("Computer action:", myAct)
            print("Point for you\n")
        else:
            print("Invalid action!!")
            print("No Points!!\n")
        i += 1

    print("Scores:\n\tComputer:", computer, "\n\tYou:", you)
    if computer > you:
        print("Computer Won!!")
    elif you > computer:
        print("You Won!!")
    else:
        print("It's tie!!")


game()
