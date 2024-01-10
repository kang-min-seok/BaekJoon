# 65~90(대문자)
# 97~122(소문자)

def ROT13(a):
    a=ord(a)
    print(a)
    if(a>=65 and a<=90 and a+13 > 90):
        print(1)
        return a+(a-77)
    elif(a>=65 and a<=90):
        print(2)
        return a+13
    elif(a>=97 and a<=122 and a+13 > 122):
        print(3)
        return a+(a-109)
    elif(a>=65 and a<=90):
        print(4)
        return a+13
    
S = input()

for i in range(len(S)):
    sibal = ROT13(S[i])
    print(sibal)