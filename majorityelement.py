nums = []

result, count = 0,0

for n in nums:
    if count == 0:
        result = n

    count += (1 if n == result else -1)

print(result)
