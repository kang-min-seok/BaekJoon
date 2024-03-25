dice = int(input())
dice_list = list(map(int, input().strip().split()))[:6]

exceptDice = [(0,5),(2,3),(1,4)]

two_sum = []
for i in range(6):
    for j in range(i+1,6):
        if (i,j) not in exceptDice:
            two_sum.append(dice_list[i] + dice_list[j])

three_sum = []
for i in range(4):
    for j in range(i+1, 5):
        for x in range(j+1,6):
            if (i,j) not in exceptDice and (j,x) not in exceptDice and (i,x) not in exceptDice:
                three_sum.append(dice_list[i] + dice_list[j] + dice_list[x])

# 0,1,2,3,4,5

minDice = min(dice_list)
minTwoDice = min(two_sum)
minThreeDice = min(three_sum)


result = 0


if(dice == 1):
    dice_list.sort()
    for i in range(5):
        result += dice_list[i]
    print(result)
else:
    result = (((dice - 2) ** 2) * 5 * minDice) + ((dice - 2) * 4 * minDice) + (minTwoDice * 4) + (minThreeDice * 4) + ((dice - 2) * 8 * minTwoDice)
    print(result)