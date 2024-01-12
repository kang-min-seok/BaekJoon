N, M = map(int, input().split())
lst = [[int(x) for x in input().split()] for _ in range(M)]	

packageLst = []
pieceLst = []

for i in range(M):
    packageLst.append(lst[i][0])
    pieceLst.append(lst[i][1])

packageLst.sort()
pieceLst.sort()

if(pieceLst[0] * 6 > packageLst[0]):
    packageNum = N // 6
    pieceNum = N % 6
    if(packageLst[0] < pieceNum * pieceLst[0]):
        result = packageLst[0] * (packageNum+1)
    else:
        result = packageLst[0] * packageNum + pieceLst[0] * pieceNum
else:
    result = pieceLst[0] * N

print(result)