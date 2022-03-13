import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

if n==1:
    print(arr[0])
else:
    for i in range(1, len(arr)):
        arr[i]=arr[i]+arr[i-1]
    print(sum(arr))
