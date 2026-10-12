import random

def craps_game():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    total = dice1 + dice2

    print("The sum of dice is", dice1, "+", dice2, "=", total)

    if total == 7 or total == 11:
        print("You won")

    elif total == 2 or total == 3 or total == 12:
        print("You lose")

    else:
        goal = total
        print("The sum goal number is", goal)

        while True:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            total = dice1 + dice2

            print("The sum of dice is", dice1, "+", dice2, "=", total)

            if total == goal:
                print("You won")
                break

            elif total == 7:
                print("You lose")
                break


craps_game()
