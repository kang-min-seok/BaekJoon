N, M = map(int, input().split())

array_2d = []

# 다음 N개의 줄에 걸쳐서 배열을 입력받음
for _ in range(N):
    row = list(map(int, input()))  # 각 줄에서 M개의 숫자를 입력받아 리스트로 변환
    array_2d.append(row)  # 변환된 리스트를 2차원 배열에 추가


def isSquare(N,M,array_2d):
    smallSize = 0
    if(N > M):
        smallSize = M
    else:
        smallSize = N


    for i in range(smallSize, 0, -1):
        if(i == 1):
            return i
        for j in range(N + 1 - i):
            for x in range(M + 1 - i):
                if(array_2d[j][x] == array_2d[j][x+i-1] == array_2d[j+i-1][x] == array_2d[j+i-1][x+i-1]):
                    return i * i


print(isSquare(N,M,array_2d))