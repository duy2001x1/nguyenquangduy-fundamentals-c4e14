prime = False

test = int(input("Enter a number to test: "))

if test < 2:
    print(test, "is not a prime number.")
elif test == 2:
    print("2 is a prime number.")

for i in range(2, test):
    if test % i == 0:
        print(test, "is not a prime number.")
        break
    elif test == i + 1:
        print(test, "is a prime number.")
