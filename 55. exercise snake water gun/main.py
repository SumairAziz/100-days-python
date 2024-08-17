import random
import math


# rNumber = lambda: math.floor(random.random() * 10 / 3.5)
rNumber = lambda: random.randint(0,2)



print("\nWelcome to Snake Water Gun Game\n".center(122))


again = "y"
total = 0


winning_combinations = [[1, 0], [0, 2], [2, 1]]

def main():
    global total
    var = int(input("\t\t0 for Gun\t\t1 for Water\t\t2 for Snake\nEnter here: "))

    
    while True:
        num = rNumber()
        if num != var:
            break

    print(f"computer generated {num}")
    choice_pair = [var, num]

    
    if choice_pair in winning_combinations:
        print("You win!")
        total += 1
    else:
        print("You lost!")

    global again
    again = input('Do you want to continue? "y" or "n": ').lower()


while again == "y":
    main()


print(f"Your total score is {total}")
