from random import randint

# num1 = randint(0, 10)
# print('x =', num1)
# num2 = randint(0, 10)
# print('y =', num2)
# print(num1 + num2)

x = randint(0, 10)
print('x =', x)
calc = str(input("Operation(+,-,*,/):" ))
y = randint(0,10)
print('y =', y)
if calc == "+":
    print(x + y)
elif calc == "-":
    print(x - y)
elif calc == "*":
    print(x * y)
else:
    print(x / y)
