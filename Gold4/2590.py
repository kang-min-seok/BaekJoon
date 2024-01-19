ONE = int(input())
TWO = int(input())
THREE = int(input())
FOUR = int(input())
FIVE = int(input())
SIX = int(input())

result = SIX
if(FIVE > 0):
    result += FIVE
    temp = 11*FIVE
    ONE -= temp

if(FOUR > 0):
    result += FOUR
    temp = 20*FOUR
    while(TWO > 0 and temp > 0):
        TWO -= 1
        temp -= 4
    if(temp>0):
        ONE -= temp

if(THREE > 0):
    rest = THREE % 4
    if(rest == 0):
        result += THREE // 4
    elif(rest == 1):
        result += (THREE // 4) + 1
        temp = 27
        index = 0
        while(TWO > 0 and temp > 0 and index < 5):
            index += 1
            TWO -= 1
            temp -= 4
        if(temp>0):
            ONE -= temp
    elif(rest == 2):
        result += (THREE // 4) + 1
        temp = 18
        index = 0
        while(TWO > 0 and temp > 0 and index < 3):
            index += 1
            TWO -= 1
            temp -= 4
        if(temp>0):
            ONE -= temp
    elif(rest == 3):
        result += (THREE // 4) + 1
        temp = 9
        if(TWO > 0):
            TWO -= 1
            temp -= 4
        ONE -= temp

if(TWO > 0):
    if(TWO % 9 != 0):
        result += (TWO // 9) + 1
        temp = 36 - ((TWO % 9) * 4)
        ONE -= temp
    else:
        result += TWO // 9

if(ONE > 0):
    if(ONE % 36 != 0):
        result += (ONE // 36) + 1
    else:
        result += ONE // 36

print(result)