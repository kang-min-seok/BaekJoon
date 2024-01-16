# N값 + M값 - (A와B의 교집합 갯수 * 2)

N, M = map(int, input().split())

A = list(map(int, input().strip().split()))[:N]

B = list(map(int, input().strip().split()))[:M]

intersection = len(list(set(A) & set(B)))

result = N + M - (intersection * 2)

print(result)