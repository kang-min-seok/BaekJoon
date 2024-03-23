import sys
input=sys.stdin.readline 
from collections import deque

def bfs(n,k):
    q = deque()

    q.append((n,k,1,False,False))

    visited_bro = [[False for _ in range(500002)] for _ in range(2)]
    visited = [[False for _ in range(500002)] for _ in range(2)]
    bro_now = k
    bro_speed = 1
    while True:
        bro_now += bro_speed
        if(bro_now>500000):
            break
        speed_oddness = bro_speed % 2
        visited_bro[speed_oddness][bro_now] = True
        bro_speed += 1

    while q:
        now, bro_now, bro_speed, wait_forward, wait_back = q.popleft()
      
        
        forward = now + 1
        back = now - 1
        teleport = now * 2
        
        bro_now += bro_speed
        speed_oddness = bro_speed % 2

        if(bro_now>500000):
            return -1
        
        if(wait_forward):
            if(back == bro_now):
                return bro_speed
            elif(forward == bro_now):
                return bro_speed
            q.append((back, bro_now, bro_speed+1,False,True))
        elif(wait_back):
            if(back == bro_now):
                return bro_speed
            elif(forward == bro_now):
                return bro_speed
            q.append((forward, bro_now, bro_speed+1,True,False))
        else:
            if(back >= 0):
                if(back == bro_now):
                    return bro_speed
                elif(visited_bro[speed_oddness][back]):
                    q.append((back, bro_now, bro_speed+1,False, True))
                elif(not visited[speed_oddness][back]):
                    q.append((back, bro_now, bro_speed+1,False, False))          
                    visited[speed_oddness][back] = True
                
            if(forward <= 500000):
                if(forward == bro_now):
                    return bro_speed
                elif(visited_bro[speed_oddness][forward]):
                    q.append((forward, bro_now, bro_speed+1,True,False))
                elif(not visited[speed_oddness][forward]):
                    q.append((forward, bro_now, bro_speed+1,False,False))          
                    visited[speed_oddness][forward] = True
            
            
            if(teleport <= 500000):
                if(teleport == bro_now):
                    return bro_speed
                elif(visited_bro[speed_oddness][teleport]):
                    q.append((teleport, bro_now, bro_speed+1,True,False))
                elif(not visited[speed_oddness][teleport]):
                    q.append((teleport, bro_now, bro_speed+1,False,False))          
                    visited[speed_oddness][teleport] = True     
            
    return -1


N, K = map(int, input().split())



if(N == K):
    print("0")
else:
    print(bfs(N,K))
