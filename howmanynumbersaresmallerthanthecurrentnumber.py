nums = [6,5,4,8]
count = 0
answer = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] != nums[j] and nums[i] > nums[j]:
            count += 1
    
    answer.append(count)
    count = 0

print(answer)