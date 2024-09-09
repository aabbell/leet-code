nums = [10,4,8,3]
answer = []
leftSum = []
rightSum = []

l,r = 0, 0

for i in range (0,len(nums)):
    if i > 0:
        l += nums[i-1]
        leftSum[i] = l

for i in range (len(nums)-1, 0):
    rnum = rightSum[r]
    rnum += nums[r]
    rightSum.insert(r-1, rnum)
    r -= 1
k = 0
while k < len(nums):
    tnum = leftSum[k] - rightSum[k]
    tnum = abs(tnum)
    answer.append(tnum)
    k += 1


print(leftSum)
print(rightSum)
print(answer)




