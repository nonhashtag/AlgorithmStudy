def search(arr, N):
    s, e = 0, len(arr)

    while s<e:
        m = (s + e) // 2
        if arr[m]==N:
            return 1
        elif N < arr[m]:
            e = m
        elif arr[m] < N:
            s = m+1
    return 0


arr_len = int(input())
arr_ = list(map(int, input().split()))
in_len = int(input())
in_ = list(map(int, input().split()))

arr_.sort()
answer = []
for i in in_:
    print(search(arr_, i))
