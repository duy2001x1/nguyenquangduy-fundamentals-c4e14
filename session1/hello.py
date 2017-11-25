yob = int(input("What's your year of birth?"))
age = 2017 - yob
print("Your age is", age)

cel = int(input("Enter the temperature in Celcius?"))
fe = cel * 1.8 + 32
print(cel, "(C) =", fe, "(F)")

total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print ("Hrs=", hours, " mins=", minutes, " secs=", secs_finally_remaining)
