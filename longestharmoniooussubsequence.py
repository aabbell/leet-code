nums = [1,3,2,2,5,2,3,7]
nums = sorted(nums)

count = 0

l,r = 0 ,1

while r < len(nums):
    if nums[r] - nums[l] == 1:
        count = max(count,r-l+1)
    if nums[r] - nums[l] <= 1:
        r += 1
    else:
        l += 1

print(count)
    

