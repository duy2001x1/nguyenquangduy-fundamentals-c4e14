sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Duy and these are my flook: ")
print(sheep, sep = ', ')
print()

sheep_boss = max(sheep)
print("Now my biggest sheep has size",sheep_boss,"!", "Let's shear it!")

ind = sheep.index(max(sheep))
default = 8
sheep[ind] = default
print("After shearing, here is my flock: ")
print(sheep, sep = ', ')
print()


months = int(input("How many months? "))
for a in range(months):
    print("MONTH", a + 1, ":")

    for i in range(len(sheep)):
        growth = sheep[i] + 50
        sheep[i] = growth
    print("One month has passed, now here is my flock: ")
    print(sheep, sep = ', ')


    sheep_boss = max(sheep)
    print("Now my biggest sheep has size",sheep_boss,"!", "Let's shear it!")

    ind = sheep.index(max(sheep))
    default = 8
    sheep[ind] = default
    print("After shearing, here is my flock: ")
    print(sheep, sep = ', ')
    print()

print("My flock has size in total: ", sum(sheep))
print("I would get ", sum(sheep), "* 2$ =", sum(sheep) * 2, "$")
