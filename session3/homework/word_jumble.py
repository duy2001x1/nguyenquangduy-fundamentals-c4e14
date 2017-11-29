import random

print("Welcome to Word Jumble!")


word = "champion"
character = list(word)
random.shuffle(character)

print(*character)
print("* " * 10)

guess = input("Your answer is: ")
if guess == word:
    print("Kinda smart! XD")
else:
    print("Oops, try again.")
