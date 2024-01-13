STICK = 64

X = int(input())

StickNum = 1
DivideStick = STICK
while(STICK > X):
    DivideStick = DivideStick // 2
    StickNum += 1

    if(STICK-DivideStick >= X):
        STICK -= DivideStick
        StickNum -= 1

print(StickNum)