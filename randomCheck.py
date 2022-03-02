import random


guess = int(input("Guess the random number!"))

number=random.randint(1,9)
chances=1

while chances < 5:
    if guess == number:
        print("Congratulations YOU WON!!!")
        break
    else:
        print("not the right guess!")
        guess = int(input("Guess the random number, one more time!"))
        chances=chances+1
if chances == 5:   
    print("YOU LOSE!!!, The number is", number)  