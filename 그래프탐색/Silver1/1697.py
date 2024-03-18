import sys
input=sys.stdin.readline 

from collections import deque

N, K = map(int, input().split())

q = deque()

visited = [False for _ in range(200002)]
q.append((N,1))

visited[N] = True


def bfs():
    while q:
        now, result = q.popleft()
        forward = now + 1
        back = now - 1
        teleport = now * 2
        if(forward <= 100000):
            if(forward == K):
                return result
            elif(not visited[forward]):
                q.append((forward,result+1)) 
                visited[forward] = True
            
        if(back >= 0):
            if(back == K):
                return result
            elif(not visited[back]):
                q.append((back,result+1))          
                visited[back] = True
            
        if(teleport <= 100000):
            if(teleport == K):
                return result
            elif(not visited[teleport] and forward != K):
                q.append((teleport,result+1))        
                visited[teleport] = True
            
    
if(N == K):
    print("0")
else:
    print(bfs())