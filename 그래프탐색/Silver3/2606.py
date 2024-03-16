from collections import deque

computer = int(input())

lines = int(input())

graph = [[False] * (computer+1) for _ in range(computer+1)]
for i in range(lines):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

visited = [False] * (computer+1)

q = deque()

def bfs(start):
    q.append(start)
    visited[start] = True
    while q:
        pop_num = q.popleft()
        for i in range(computer):
            if(graph[pop_num][i+1] and not visited[i+1]):
                q.append(i+1)
                visited[i+1] = True

bfs(1)

count = 0
for i in visited:
    if(i):
        count += 1

print(count-1)