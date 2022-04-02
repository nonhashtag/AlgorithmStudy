import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))
gas.pop()

answer = gas[0]*dist[0]
bargain, locate = 0, 1

while locate < N-1:
    if gas[bargain] < gas[locate]:
        answer += gas[bargain] * dist[locate]
    else:
        answer += gas[locate] * dist[locate]
        bargain = locate
    locate += 1

print(answer)
