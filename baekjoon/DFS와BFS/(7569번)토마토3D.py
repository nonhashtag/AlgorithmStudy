import sys
from collections import deque

def bfs(graph, queue, w, h, l):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    cnt = -1
    while queue:
        cnt+=1
        for _ in range(len(queue)):
            z,y,x = queue.popleft()
            for i in range(6):
                nextX = x + dx[i]
                nextY = y + dy[i]
                nextZ = z + dz[i]
                if nextX>=0 and nextY>=0 and nextZ>=0 and nextX<w and nextY<h and nextZ<l:
                    if graph[nextZ][nextY][nextX]==0:
                        queue.append((nextZ, nextY, nextX))
                        graph[nextZ][nextY][nextX] = graph[z][y][x] + 1

    return cnt

x, y, z = map(int, sys.stdin.readline().split())
graph = [[] for z1 in range(z)]
queue = deque()

for i in range(z):
    for j in range(y):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(z):
    for j in range(y):
        for k in range(x):
            if graph[i][j][k]==1:
                queue.append((i,j,k))

answer = bfs(graph, queue, x, y, z)

for gra in graph:
    for g in gra:
        if 0 in g:
            answer=-1
            break
print(answer)

'''
for gra in graph:
    print("#"*20)
    for g in gra:
        print(g)
'''