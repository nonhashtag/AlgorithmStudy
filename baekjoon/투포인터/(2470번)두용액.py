import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
start, end = 0, N-1
h, t = 0, N-1

while start<end:
    if abs(arr[start] + arr[end]) <= abs(arr[h] + arr[t]):
        h=start; t=end

    if arr[start]+arr[end] > 0:
        end-=1
    elif arr[start]+arr[end] < 0:
        start+=1
    elif arr[start]+arr[end]==0:
        h = start; t = end
        break

print(f"{arr[h]} {arr[t]}")
