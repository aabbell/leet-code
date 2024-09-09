temperature =answer = []
count = 1

for i in range (len(temperature)):
    for j in range (1,len(temperature)):
        if temperature[i] < temperature[j]:
            answer.append(count)
            count = 1
            print(answer)
            break
        elif temperature[i] > temperature[j]:
            count+=1
            print(answer)
        else:
            answer.append(count)
            print(answer)

print(answer) [73,74,75,71,69,72,76,73]
