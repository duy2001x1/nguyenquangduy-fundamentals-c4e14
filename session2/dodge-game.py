from random import randint

x = int(randint(1,6))
print("Damage:", x)
a = int(randint(0,2))
l = int(randint(0,2))

s = a + l
print("Dodging Ability:", s)
if x < s:
    print("Dodge!")
else:
    print("Hit!")
