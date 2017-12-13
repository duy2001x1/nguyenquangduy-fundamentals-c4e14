from ex11 import *

result1 = is_inside([100, 120], [140, 60, 100, 200])
if result1 == False:
    print("Your function is correct")
else:
    print("Oops, bug 1")

result2 = is_inside([200, 120], [140, 60, 100, 200])
if result2 == True:
    print("Your function is correct")
else:
    print("Oops, bug 2")
