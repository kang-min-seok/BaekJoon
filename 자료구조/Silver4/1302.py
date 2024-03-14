from collections import Counter

N = int(input())

bookList = []
for i in range(N):
    book = input()
    bookList.append(book)

bookCount = {}
for i in bookList:
    try: bookCount[i] += 1
    except: bookCount[i ] = 1

values = bookCount.values()
max_value = max(values)

keys_with_value = [key for key, value in bookCount.items() if value == max_value]

keys_with_value.sort()

print(keys_with_value[0])