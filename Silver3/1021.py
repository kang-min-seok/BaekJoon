import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

popList = list(map(int, input().strip().split()))[:M]

queue = deque(range(1, N + 1))

result = 0
for pop in popList:
    firstIndex = queue[0]
    tempQueue = queue.copy()
    rightMove = 0
    while(True):
        firstIndex = tempQueue[0]
        if(firstIndex == pop):
            break
        tempQueue.rotate(-1)
        rightMove += 1


    tempQueue = queue.copy()
    leftMove = 0
    while(True):
        firstIndex = tempQueue[0]
        if(firstIndex == pop):
            break
        tempQueue.rotate(1)
        leftMove += 1

    if(rightMove<leftMove):
        queue.rotate(-rightMove)
        queue.popleft()
        result+=rightMove
    else:
        queue.rotate(leftMove)
        queue.popleft()
        result+=leftMove
        

print(result)