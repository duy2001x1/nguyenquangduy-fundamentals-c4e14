# print("Hi there, here is your favourite list: ")
#
# menu = ['AKM', 'M16A4', 'M416']
# for i in range(len(menu)):
#     print(i + 1, menu[i], sep=". ")
# loop = True
# while loop:
#     delpart = int(input("Enter postion to get rid of: "))
#     if delpart > len(menu) or delpart < 1:
#         print("Sorry, only items in list are available.")
#     else:
#         del menu[delpart - 1]
#
#         for i in range(len(menu)):
#             print(i + 1, menu[i], sep=". ")
#         loop = False


print("Hi there, here is your favourite list: ")

menu = ['AWM', 'M24', 'M249']
for i in range(len(menu)):
    print(i + 1, menu[i], sep=". ")
loop = True
while loop:
    delpart = input("Enter a thing to get rid of: ")
    if delpart in menu:
        menu.remove(delpart)

        for i in range(len(menu)):
            print(i + 1, menu[i], sep=". ")
    else:
        print("Sorry, only items in list are available.")
    loop = False
