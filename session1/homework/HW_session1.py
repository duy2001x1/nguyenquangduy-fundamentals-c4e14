1.
- Use a function called "type": type(variable)
Example:
>>> a = 3
>>> type(a)
<class 'int'>

- When you give a variable an illegal name: does not begin with a letter or a underscore, contain an illegal character or Python keywords, you will get SyntaxError from the compiler telling you that some of your variables have invalid names.
Examples:
>>> 1511fday = "It's over" -> invalid name because it begins with a number
>>> duTy$ = 2509 -> invalid name because it contains illegal characters, the dollar sign
>>> lambda = "Rum" -> invalid name because lambda is one of the Python keywords

2.
r = int(input("Radius?"))
a = r * r * 3.14
print("Area =", a)

3.
cel = int(input("Enter the temperature in Celcius?"))
fe = cel * 1.8 + 32
print(cel, "(C) =", fe, "(F)")

4. turtle
a. square
from turtle import *
color("grey")
shape("turtle")
speed(-1)
for i in range(4):
    forward(200)
    left(90)
mainloop()

b. triangle
from turtle import *
color("grey")
shape("turtle")
speed(-1)
for i in range(3):
    forward(200)
    left(120)
mainloop()

c. a circle
from turtle import*
color("grey")
shape("turtle")
speed(-1)
circle(100)
mainloop()

d. multi-circles
from turtle import*
color("grey")
shape("turtle")
speed(-1)
for i in range(6):
  circle(100)
  left(60)
mainloop()

e. a bunch of circles again
from turtle import*
color("grey")
shape("turtle")
speed(-1)
for i in range(50):
  circle(100)
  left(10)
mainloop()
