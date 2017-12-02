initial_num = int(input("How many B bacterias are there? "))

time_mins = int(input("How much time in minutes will we wait? "))

total_num = initial_num * 2 ** (time_mins // 2)
print("After {0} minutes, we would have {1} bacterias.".format(time_mins, total_num))
