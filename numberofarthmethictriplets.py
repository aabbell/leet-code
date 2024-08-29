nums = [4,5,6,7,8,9]

diff = 2
count = 0

for i in range(0,len(nums)):
    for j in range (1,len(nums)):
        for k in range (2,len(nums)):
            if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                count += 1

print(count)