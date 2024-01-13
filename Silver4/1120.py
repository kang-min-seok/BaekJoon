A, B = map(str, input().split())


temp=0
if(len(B)-len(A) == 0):
    dif = 0
    for i in range(len(A)):
        if(A[i] != B[i]):
            dif += 1
    temp = dif
else:
    for i in range(len(B)-len(A)+1):
        dif = 0
        for j in range(len(A)):
            if(A[j] != B[j+i]):
                dif += 1
        if(i == 0):
            temp = dif
        elif(dif<temp):
            temp = dif
    
     
print(temp)