s = "nwcn"
answer = []
s = list(s)

for i in range(1,len(s)):
    answer.append(s[i-1])
    if s[i] in answer:
        print(s[i])
        break




