import sys

#이진탐색으로 가자..
def search(arr, x):
    start, end = 0, len(arr)-1
    cnt = 0
    while start<end:
        temp = arr[start] + arr[end]

        if x < temp:
            end-=1
            continue
        if x == temp:
            cnt+=1
        start+=1
    return cnt



N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()

print(search(arr, x))
