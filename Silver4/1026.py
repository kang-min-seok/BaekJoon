n = int(input().strip())

line2 = list(map(int, input().strip().split()))[:n]

line3 = list(map(int, input().strip().split()))[:n]

line2.sort()
line3.sort(reverse=True)

result = 0

for i in range(n):
    result += line2[i] * line3[i]

print(result)