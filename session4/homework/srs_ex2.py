numbers = [1, 6, 8, 1, 2, 1, 5, 6]

x = int(input("Enter a number: "))

appear = 0
exist = False
found = False

for i in range(len(numbers)):
    if x == numbers[i]:
        found = True
        appear += 1
        exist = True

if exist == True:
    print("{0} appears {1} time(s) in my list.".format(x, appear))
else:
    print("Not Found")
