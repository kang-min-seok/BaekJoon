def digitcf(num):
    return list(map(int, str(num)))


N = int(input())

index = 0
result = 0

if(N <= 10):
    result = N
elif(N >= 1023):
    result = -1
else:
    index = 11
    result = 20
    while(True):
        numList = digitcf(result)
        isDec = False
        for i in range(len(numList)-1):
            if(numList[i]>numList[i+1]):
                isDec = True
            else: 
                isDec = False
                numList[i] = numList[i]+1
                numList[i+1] = 0
                result = int(''.join(map(str, numList)))
                break   
        if(isDec):
            if(index == N):
                break
            index += 1
            result += 1

print(result)