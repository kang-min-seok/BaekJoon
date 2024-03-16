from collections import deque

N = int(input())

parent_result, son_result = map(int, input().split())

family_num = int(input())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)


for i in range(family_num):
    parent, son = map(int, input().split())
    graph[parent][son] = True
    graph[son][parent] = True

def bfs(start_num):
    q = deque()
    q.append(start_num)
    visited[start_num] += 1
    while q:
        now_num = q.popleft()
        for i in range(N):
            if(graph[now_num][i+1] and visited[i+1] == 0):
                q.append(i+1)
                visited[i+1] = visited[now_num] + 1
        if(visited[parent_result] != 0 and visited[son_result] != 0):
            return visited[now_num]
    return -1

print(bfs(parent_result))