import numpy as np
from collections import deque

M, N, H = map(int, input().split())



tomatoBox = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

graph = [[False] * ((M*N*H)+1) for _ in range((M*N*H)+1)]


for i in range(H):
    for j in range(N):
        tomatoBox[i][j] = list(map(int, input().strip().split()))[:M]

tomatoBox = [element for sublist1 in tomatoBox for sublist2 in sublist1 for element in sublist2]

print(tomatoBox)

for i in range(1,((M*N*H)+1)):
    if(tomatoBox[i-1] != -1):
        if(tomatoBox[i] != -1 and i % M != 0):
            graph[i][i+1]=True
            graph[i+1][i]=True
        
        if(tomatoBox[i] != -1 and i % M != 0):
            graph[i][i+1]=True
            graph[i+1][i]=True
            

# 높이, 세로, 가로