m = 6
n = 10

for i in range(m):
    for a in range(n):
        if (i + a) % 2 == 0:
            print(" *", end = "")
        else:
            print(" x", end = "")
    print()
