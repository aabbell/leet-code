operations = ["X++","++X","--X","X--"]
answer = 0

for i in range(0,len(operations)):
    if operations[i] == "--X":
        answer -= 1
    elif operations[i] == "X--":
        answer -= 1
    elif operations[i] == "X++":
        answer += 1
    elif operations[i] == "++X":
        answer += 1

print(answer)
