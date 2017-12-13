dictionary = {
    'eny' : 'em người yêu',
    'hk' : 'không',
    'ns' : 'nói',
    'xm' : 'xem'
}

loop = True
while loop:
    for key, value in dictionary.items():
        print(key, end = ' ')
    print()

    code = str(input("Code: ")).lower()
    print("* " * 10)

    if code in dictionary:
        print("Translation: ", dictionary[code])
    elif code == 'quit':
        loop = False
    else:
        choice = input("Not Found. Do you want to contribute (Y/N)? ").lower()
        if choice == 'y' or choice == 'Y':
            translation = input("Translation: ")
            dictionary[code] = translation
