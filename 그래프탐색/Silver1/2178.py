from collections import deque

N, M = map(int, input().split())

graph = [[int(digit) for digit in input()] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()

def bfs(x, y):
    result = 0
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        result += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=nx<M and 0<=ny<N and graph[ny][nx] == 1):
                queue.append((nx,ny))
                graph[ny][nx] = graph[y][x] + 1
        
    return(graph[N-1][M-1])
print(bfs(0,0))