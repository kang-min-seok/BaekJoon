N, M, X = map(int, input().split())


def isMeet(M, X):
    roundNum = 1
    while(True):
        smallSize = 0
        if(M > X):
            smallSize = X
        else:
            smallSize = M

        if(smallSize % 2 == 1 and abs(M-X) == 1):
            return roundNum
        
        if(M%2==1):
            M+=1

        if(X%2==1):
            X+=1

        M = M / 2
        X = X / 2

        roundNum += 1

print(isMeet(M, X))