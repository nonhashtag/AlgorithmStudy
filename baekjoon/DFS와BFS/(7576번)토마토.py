import sys
from collections import deque

# BFS 같은 queue를 이용한 문제의 경우 list보다 deque가 더 빠르다.
def bfs(graph, q, w, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while len(q)>0:
        y, x = q.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0<=nextX and nextX<w and 0<=nextY and nextY<h:
                if graph[nextY][nextX]==0:
                    graph[nextY][nextX] = graph[y][x] + 1
                    q.append((nextY, nextX))


w, h = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
q = deque()

for i in range(h):
    for j in range(w):
        if graph[i][j]==1:
            q.append((i,j))

bfs(graph, q, w, h)
answer = 0
for g in graph:
    if 0 in g:
        answer=-1
        break
    for c in g:
        answer = answer if answer>=c else c


print(answer-1 if answer!=-1 else -1)
