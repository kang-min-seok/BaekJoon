from collections import deque

def bfs(start_x, start_y):
    q = deque()
    house_num = 1
    q.append((start_x,start_y))
    graph[start_y][start_x] += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=nx<N and 0<=ny<N and graph[ny][nx] == 1):
                q.append((nx,ny))
                graph[ny][nx] += house_num
                house_num += 1
    return house_num


N = int(input())

graph = [[int(digit) for digit in input()] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]



result = []

for y in range(N):
    for x in range(N):
        if(graph[y][x] == 1):
            result.append(bfs(x,y))

result.sort()

print(len(result))

for i in result:
    print(i)