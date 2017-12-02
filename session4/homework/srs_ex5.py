initial_pair = 1

a = initial_pair
b = 0

for i in range(5):
    c = b + a
    print("Month {0}: {1} pair(s) of rabbit.".format(i, c))
    b = a
    a = c
