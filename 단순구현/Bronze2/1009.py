T = int(input())

resultResult = []
for i in range(T):
    N, M = map(int, input().split())
    N_index = N % 10
    index = M % 4
    if(index == 0):
        index = 4
    square = N_index ** index
    if(square % 10 == 0):
        resultResult.append('10')
    else:
        resultResult.append(square % 10)

for i in resultResult:
    print(i)