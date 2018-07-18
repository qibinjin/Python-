nums = [-1, 0, 1, 2, -1, -4]
ret = set()
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):

            if nums[i] + nums[j] + nums[k] == 0:
                if nums[i] <= nums[j] <= nums[k]:
                    ret.add((nums[i], nums[j], nums[k]))
                else:
                    if nums[j] >= nums[k]:
                        if nums[i] <= nums[k]:
                            ret.add((nums[i], nums[k], nums[j]))
                        else:
                            if nums[i] <= nums[j]:
                                ret.add((nums[k], nums[i], nums[j]))
                            else:
                                ret.add((nums[j], nums[k], nums[i]))

                    else:
                        if nums[i] <= nums[k]:
                            ret.add((nums[j], nums[i], nums[k]))
                        else:
                            ret.add((nums[j], nums[k], nums[i]))

for i in ret:
    print(i)
