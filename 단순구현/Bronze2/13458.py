N = int(input())
A = list(map(int, input().strip().split()))[:N]
B, C = map(int, input().split())

result = N

for i in A:
    i -= B
    if(i>0):
        if(i % C == 0):
            result += i//C
        else:
            result += (i//C) + 1

print(result)