import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp0 = [1, 0]
dp1 = [0, 1]
MAX = max(arr)

for i in range(2, MAX+1):
    dp0.append(dp0[i-1]+dp0[i-2])
    dp1.append(dp1[i-1]+dp1[i-2])

for i in arr:
    print(f"{dp0[i]} {dp1[i]}")
