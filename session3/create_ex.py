print("Hi there, here is your favourite things so far!")
things = ['games', 'SAT', 'gear']
print(*things, sep=', ')
things.append(input("Name one thing to add: "))
print(*things, sep=', ')
