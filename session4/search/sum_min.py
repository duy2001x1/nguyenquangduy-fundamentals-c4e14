nums = [-1, -25, 1, 35, 25, 35, -40, 71, 99]

min_num = nums[0]

for num in nums:
    if min_num > num:
        min_num = num

print("Min =", min_num)

# print(sum(nums))

# print(min(nums))
