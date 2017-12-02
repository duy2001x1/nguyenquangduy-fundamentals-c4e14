import random

wordlist = ['champion', 'something', 'miracle', 'uniform', 'chess', 'basketball', 'chef', 'gameshow', 'marriage', 'spicy']

print("Welcome to Word Jumble!")

life = 5

play = input("Do you want to play?")
if play == "yes":
    loop1 = True
    while loop1:
        word = random.choice(wordlist)
        print("You have",life,"chances!")
        loop2 = True
        while loop2:
            character = list(word)
            character_hint = list(word)
            random.shuffle(character)

            print(*character)
            print("* " * 10)

            guess = input("Your answer is: ")
            if guess == word:
                print("Kinda smart! XD")
                wordlist.remove(word)
                loop2 = False
            elif guess == "skip":
                print("The word is:", word)
                loop2 = False
            elif guess == "quit":
                print("Bye bye!")
                loop2 = False
                loop1 = False
            elif guess == "hint":
                place = int(input("Place to show? "))
                print(character_hint[place - 1])
            else:
                print("Oops, try again.")
                left = life - 1
                print(left,"left!")
                life = left
                if left == 0:
                    print("You suck :<")
                    loop2 = False
                    loop1 = False
else:
    print("See ya later.")
