import sys
import heapq

N = int(sys.stdin.readline())
ropes = []

for i in range(N):
    heapq.heappush(ropes, int(sys.stdin.readline()))

answer = len(ropes) * ropes[0]
heapq.heappop(ropes)
for i in range(len(ropes)):
    if answer < ropes[0]*len(ropes):
        answer = ropes[0]*len(ropes)
        heapq.heappop(ropes)

print(answer)
