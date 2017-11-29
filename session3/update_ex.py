print("Hi there, here is your favourite list: ")
menu = ['jung', 'mid', 'top']
for i in range(len(menu)):
    print(i + 1, menu[i], sep=". ")
pos = int(input("Position you want to update: "))
repl = input("Your replacement: ")
menu[pos - 1] = repl

for i in range(len(menu)):
    print(i+1, menu[i], sep=". ")
