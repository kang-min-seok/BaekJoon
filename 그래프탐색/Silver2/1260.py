from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfsVisited = [False] * (N+1)
bfsVisited = [False] * (N+1)


def dfs(v):
    dfsVisited[v] = True

    print(v, end=" ")

    for i in range(1, N+1):
        if(not dfsVisited[i] and graph[v][i] == 1):
            dfs(i)

def bfs(v):
    q = deque()

    bfsVisited[v] = True
    q.append(v)
    while(q):
        print(q[0], end=" ")
        for i in range(1,N+1):
            if(not bfsVisited[i] and graph[q[0]][i] == 1):
                bfsVisited[i] = True
                q.append(i)

        q.popleft()
dfs(V)
print("")
bfs(V)