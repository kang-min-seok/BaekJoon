values = []

for i in range(9):
    value = input()
    values.append(int(value))

sum = 0
for i in range(9):
    sum = sum + int(values[i])

break_out = False

for j in range(9):
    for x in range(1,9-j):
        if(sum - values[j] - values[j + x] == 100):
            deleteNum = values[j]
            deleteNum2 = values[j+x]
            values.remove(deleteNum) 
            values.remove(deleteNum2)
            break_out = True
            break

    if break_out:
        break 

values.sort()

for i in range(7):
    print(values[i])
