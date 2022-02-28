#이분탐색 문제인데 이분탐색은 시간초과, 해싱은 통과됨
"""
N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
own = list(map(int, input().split()))

def starting(arr, N):
    s, e = 0, len(arr)-1
    while s<e:
        m = (s+e)//2

        if arr[m] < N:
            s = m+1
        else:
            e = m
    m = (s+e)//2
    return m if arr[m]==N else -1

def ending(arr, N):
    s, e = 0, len(arr)-1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= N:
            s = m + 1
        elif N < arr[m]:
            e = m - 1

    m = (s+e)//2
    return m if arr[m]==N else -1

answer = ""
for i in own:
    if starting(arr, i)>=0:
        print(ending(arr, i) - starting(arr, i) + 1, end=' ')
    else:
        print(0, end=' ')
"""


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
own = list(map(int, input().split()))

answer = dict()
for i in arr:
    answer.setdefault(i, 0)
    answer[i]+=1

print(' '.join(str(answer[i]) if i in answer else '0' for i in own))
