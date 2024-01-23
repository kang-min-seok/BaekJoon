def isPrimeNumber(Number):
    if(Number % 2 == 0):
        return False
    else:
        for i in range(3,Number//2,2):
            if(Number % i == 0):
                return False
    return True

def isAmazingNumber(stack, digit, index):
    result = []
    if(digit == index):
        for x in stack:
            print(x)
        return stack
    else:
        for i in stack:
            for j in [1,3,7,9]:
                checkNumber = str(i) + str(j)
                if(isPrimeNumber(int(checkNumber))):
                    result.append(int(checkNumber))

    
    isAmazingNumber(result, digit, index+1)



N = int(input())

basic = [2,3,5,7]
if(N == 1):
    for i in basic:
        print(i)
else:
    isAmazingNumber(basic, N, 1)