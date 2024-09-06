nums = [1,1,1,1,1]

answer = []

answer.append(nums[0])

for i in range (1 , len(nums)):
     num = answer[i-1] + nums[i]
     answer.append(num)

print(answer)