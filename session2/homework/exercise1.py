hcm = int(input("Your height(cm): "))
w = int(input("Your weight(kg): "))
hm = hcm/100

bmi = w/(hm * hm)

if bmi < 16:
    print("You are severely underweight.")
else:
    if bmi <= 18.5:
        print("You are underweight.")
    else:
        if bmi <= 25:
            print("You are normal.")
        else:
            if bmi <= 30:
                print("You are overweight!")
            else:
                print("Obesity!!!")
