import sys

def brutal(arr):
    prev = 0
    cnt = 0
    for end, start in arr:
        if prev <= start:
            cnt += 1
            prev = end
            #print(f"{start} {end}")
        else:
            continue
    return cnt

N = int(input())
cur = N-1
meet = []
for i in range(N):
    #반복문에서의 input과 sys.stdin.readline()의 속도차이는 어마어마하다.
    start, end = map(int, sys.stdin.readline().split())
    meet.append((end, start))
meet.sort()
print(brutal(meet))