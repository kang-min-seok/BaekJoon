# 내가 짠 코드
N = int(input())

def minBag():
        
    fiveTry = N // 5
    if(N == 3):
        return 1
    elif(N == 4):
        return -1
    else:
        threeRest = -1
        for i in range(fiveTry,-1,-1):
            threeRest += 1
            fiveRest = N - (5 * i)
            if(fiveRest == 0):
                return i
            if(fiveRest % 3 == 0):
                return fiveTry - threeRest + fiveRest // 3
        return -1

print(minBag())

# --------------------------------------------------------------------
# 깔끔한 인터넷 코드
# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)