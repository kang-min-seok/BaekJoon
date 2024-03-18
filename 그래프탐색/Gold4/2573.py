import sys
input=sys.stdin.readline 

from collections import deque

N, M = map(int, input().split())

ice_map = []

for _ in range(N):
    ice_map.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    q = deque()
    result = 0
    while True:
        result_graph = [[0]* M for _ in range(N)]
        for result_y in range(N-2):
            for result_x in range(M-2):
                if(ice_map[result_y+1][result_x+1]!=0):
                    result_graph[result_y+1][result_x+1] = 1

        loop_break = False

        for y in range(N-2):
            for x in range(M-2):
                if(ice_map[y+1][x+1] != 0):
                    q.append((x+1,y+1))
                    result_graph[y+1][x+1] += 1
                    loop_break = True
                    break
            if loop_break:
                break
            
        graph = [[0]* M for _ in range(N)]
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if(ice_map[ny][nx] == 0):
                    graph[y][x] += 1
                elif(ice_map[ny][nx] != 0 and result_graph[ny][nx] == 1):
                    q.append((nx,ny))
                    result_graph[ny][nx] += 1 # 방문처리
                    
        finish_test = True

        for result_y in range(N-2):
            for result_x in range(M-2):
                if(result_graph[result_y+1][result_x+1] == 1):
                    return result
                elif(result_graph[result_y+1][result_x+1] == 2):
                    finish_test = False

                ice_map[result_y+1][result_x+1] = ice_map[result_y+1][result_x+1] - graph[result_y+1][result_x+1]
                if(ice_map[result_y+1][result_x+1]<0):
                    ice_map[result_y+1][result_x+1] = 0

        if(finish_test):
            return 0

        result += 1
        


print(bfs())
