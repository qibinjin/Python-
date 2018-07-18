nums = [4,4, 5, 1, 2, 3]
target = 4
for i in range(len(nums)):
    if nums[i] == target:
        print(True)
        break
else:
    print(False)