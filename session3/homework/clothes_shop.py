print("Welcome to our shop!")
clothes = ['T-Shirt', 'Sweater']
print("Our items: ", end = "")
print(*clothes, sep = ', ')
print("* " * 10)

loop = True
while loop:
    func = input("Which function do you want (C, R, U, D)?")
    if func == "C" or func == "c":
        clothes.append(input("Enter new item: "))
        print("Our items: ", end = "")
        print(*clothes, sep = ', ')
        print("* " * 10)
    elif func == "R" or func == "r":
        print("Our items: ", end = "")
        print(*clothes, sep = ', ')
        print("* " * 10)
    elif func == "U" or func == "u":
        up_pos = int(input("Update position: "))
        repl = str(input("New item: "))
        clothes[up_pos] = repl
        print("Our items: ", end = "")
        print(*clothes, sep = ', ')
        print("* " * 10)
    elif func == "D" or func == "d":
        del_pos = int(input("Delete position: "))
        del clothes[del_pos - 1]
        print("Our items: ", end = "")
        print(*clothes, sep = ', ')
    elif func == "quit":
        loop = False
    else:
        print("Sorry, this function has not been supported yet.")
        loop = False
