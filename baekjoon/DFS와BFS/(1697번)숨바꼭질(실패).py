import sys
from collections import deque

def bfs(q, visited, target):
    walk = [-1, 1, 0]
    tel = [1, 1, 2]
    cnt=0
    while len(q)>0:
        for n in range(len(q)):
            cur = q.popleft()
            if cur==target:
                return cnt
            visited[cur]=1
            for i in range(3):
                nextX = (cur + walk[i]) * tel[i]
                if 0 <= nextX and nextX <= 100000:
                    if visited[nextX]==0:
                        q.append(nextX)
        cnt += 1

N, K = map(int, sys.stdin.readline().split())
visited = [0]*100001
q = deque()
q.append(N)
print(bfs(q, visited, K))
