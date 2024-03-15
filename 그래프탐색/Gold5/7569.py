from collections import deque

M, N, H = map(int, input().split())


tomatoBox = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomatoBox[i][j] = list(map(int, input().strip().split()))[:M]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()

# 높이, 세로, 가로

def bfs():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if(tomatoBox[z][y][x] == 1):
                    queue.append((z,y,x))
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if(0<=nx<M and 0<=ny<N and 0<=nz<H and tomatoBox[nz][ny][nx]==0):
                queue.append((nz,ny,nx))
                tomatoBox[nz][ny][nx] = tomatoBox[z][y][x] + 1
    
    max = 1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if(tomatoBox[z][y][x] > max):
                    max = tomatoBox[z][y][x]
                elif(tomatoBox[z][y][x] == 0):
                    return -1
    if(max == 1):
        return 0
    return max-1

print(bfs())