numbs = [7, 9, 20, 25, 1, 66, 51, 49, 72, 87]
x = int(input("Enter a number: "))

found = False
found_index = -1

for index, numb in enumerate(numbs):
    if numb == x:
        found_index = index
        found = True
        break

if not found:
    print("Not found")
else:
    print("Found {0} at index {1}".format(x,found_index))
