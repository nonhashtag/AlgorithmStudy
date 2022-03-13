import sys

n, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
answer = 0

for i in range(n):
    c = arr.pop()
    div = k//c
    answer += div
    k -= div*c

    if k==0:
        break

print(answer)
