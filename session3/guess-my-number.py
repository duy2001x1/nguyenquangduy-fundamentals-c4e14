# count = 0
# while count < 3:
#     print("Running ...")
#     count += 1

from random import randint

number = randint(0, 100)

guess_wrong = True

while guess_wrong:
    guess = int(input("Enter a number(0-100): "))
    if guess > number:
        print("Smaller")
    elif guess < number:
        print("Larger")
    else:
        print("Bingo!!!")
        guess_wrong = False
