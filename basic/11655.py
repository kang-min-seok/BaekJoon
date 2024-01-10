# 65~90(대문자)
# 97~122(소문자)

def ROT13(a):
    a=ord(a)
    if 65 <= a <= 90: 
        if (a+13>90):
            return chr(65+(a-78))
        else:
            return chr(a+13)
    elif 97 <= a <= 122: 
        if (a+13>122):
            return chr(97+(a-110))
        else:
            return chr(a+13)
    else:
        return chr(a)

        
    
S = input()

result = ""
for i in range(len(S)):
    Y = ROT13(S[i])
    result = result+Y

print(result)