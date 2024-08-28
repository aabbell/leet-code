def smallestEvenMultiple(n):
    for i in range(1,n+1):
        num = i * n
        if num % 2 == 0 and num % n == 0:
            print(num)
            break 
        else:
            print(1)

smallestEvenMultiple(1)


