def fizzbuzz(self,n):
    mylist = []
    for i in range(1,n+1):
        if i % 3 == 0  and i % 5 == 0:
            mylist.append("FizzBuzz")
        elif i % 3 == 0:
            mylist.append("Fizz")
        elif i % 5 == 0:
            mylist.append("Bizz")
        else:
            mylist.append(str(i))
    return mylist
