import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().strip().split()))[:N] for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if(map[i][j] == 1):
            house.append([i+1,j+1])
        if(map[i][j] == 2):
            chicken.append([i+1,j+1])
    
finalChicken = list(combinations(chicken,M))


chickenLength = []
finalChickenLength = []

for c in finalChicken:
    chickenResult = []
    for h in house:
        for i in range(M):
            chickenSum = abs(c[i][0] - h[0]) + abs(c[i][1] - h[1])
            chickenLength.append(chickenSum)
        chickenLength.sort()
        chickenResult.append(chickenLength[0])
        chickenLength = []
    finalChickenLength.append(sum(chickenResult))
finalChickenLength.sort()
print(finalChickenLength[0])