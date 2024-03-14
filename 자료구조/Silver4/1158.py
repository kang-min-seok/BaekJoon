N, K = map(int, input().split())

defArray = []

for i in range(N):
    defArray.append(i+1)

newArray = []
removeIndex = 0
for i in range(N):
    if(removeIndex + K > len(defArray)):
        if((removeIndex + K) % len(defArray) == 0):
            removeIndex = len(defArray) - 1
        else:    
            removeIndex = (removeIndex + K) % len(defArray)-1
    else:
        removeIndex = removeIndex + K - 1

    newArray.append(defArray[removeIndex])
    defArray.pop(removeIndex)
    

result_str = ', '.join(str(x) for x in newArray)


print(f'<{result_str}>')