1. A Boolean value is either true or false
example:
print(1 > 2)
print(10 == 10)
print(6 != 9)

2. A flow chart is a standard way to plan code. It is a type of diagram that represents your code.

3. Nested conditionals is the way you use if or else statement inside another if or else statementself.
example:
a = int(input("Your age: "))
b = int(input("Your crush's age: "))
c = a - b
if c < 4:
    print("You guys are definitely gonna be a perfect couple!")
else:
    if c == 4:
        print("Friendzone.")
    else:
        print("Wouldn't work :<")
