operations = ["5","-2","4","C","D","9","+","+"]
op = []
for i in range(len(operations)):
    if operations[i] == '+':
        op[-1] = int(op[-1])
        op [-2] = int(op[-2])
        add = op[-1] + op[-2]
        op.append(add)
    elif operations[i] == 'C':
        op.pop()
    elif operations[i] == 'D':
        op[-1] = int(op[-1])
        multi = op[-1] * 2
        op.append(multi)
    else:
        op.append(operations[i])
    print(op)

for k in range(0,len(op)):
    op[k] = int(op[k])

sums = sum(op)
print(sums)
    
