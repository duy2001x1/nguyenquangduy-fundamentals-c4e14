nums = [-99, -23, 0, 12, 34, 62, 98, 123]

x = int(input("Find the number: "))

found = False
lo = 0
hi = len(nums)

while hi > lo:
    mid = (lo + hi)//2
    num = nums[mid]

    if x == num:
        found = True
        break
        print("Found")
    elif x < num:
        hi = mid
        print("Left")
    elif x > num:
        lo = mid + 1
        print("Right")

if not found:
    print("Not Found")
