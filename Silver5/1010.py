# 첫줄은 경우의 수 T가 주어짐
# 두번쨰 줄부터 N, M값이 주어지고 T값만큼 줄갯수
# M * (M-1) ... (M-(n-1)) <- N개 만큼 이런식으로 곱함
# 위 값에 N / N-1 / N-2 ... / 1 까지 나눔
from math import gcd

T = int(input())

resultList = []
for i in range(T):
    N, M = map(int, input().split())
    result = 1
    numerator = 1
    denominator = 1
    for j in range(N):  
        numerator *= (M - j)
        denominator *= (N - j)
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    result = result * numerator // denominator

    resultList.append(int(result))

for k in resultList:
    print(k)
