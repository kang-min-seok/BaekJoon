N = int(input())
F = int(input())

a = []
for i in str(N):
    a.append(i)

a[-1] = "0"
a[-2] = "0"

number = int("".join(a))

while(number % F != 0):
    number += 1

result = []
for i in str(number):
    result.append(i)

print(result[-2]+result[-1])