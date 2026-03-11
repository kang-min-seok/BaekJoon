N, M = map(int, input().split())
arr= list(map(int, input().strip().split()))[:N]

def bubble_sort(arr):
    k = 0
    for i in range(N):
        is_sorted = True
        for j in range(N - i - 1):
            if (arr[j] > arr[j+1]):
                is_sorted = False
                k += 1
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            if (k == M):
                print(str(arr[j]) + " " + str(arr[j+1]))
                return
        if (is_sorted):
            print("-1")
            return
    print("-1")

bubble_sort(arr)