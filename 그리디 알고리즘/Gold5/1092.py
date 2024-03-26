crain = int(input())
crain_list = list(map(int, input().strip().split()))[:crain]

box = int(input())
box_list = list(map(int, input().strip().split()))[:box]

crain_list.sort(reverse=True)
box_list.sort(reverse=True)

result = 0
if(box_list[0] > crain_list[0]):
    print("-1")
else:
    while True:
        for i in range(len(crain_list)):
            for j in range(len(box_list)):
                if(crain_list[i]>=box_list[j]):
                    del box_list[j]
                    break
        result += 1
        if(len(box_list)==0):
            break
    print(result)
        
    