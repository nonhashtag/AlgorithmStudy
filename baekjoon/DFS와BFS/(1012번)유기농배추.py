import sys

# 기본 재귀호출횟수로는 부족함..
sys.setrecursionlimit(10000)

def dfs(graph, y, x, h, w):
    graph[y][x] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if 0<=nextX and nextX<w and 0<=nextY and nextY<h:
            if graph[nextY][nextX]==1:
                dfs(graph, nextY, nextX, h, w)

def bfs(graph, y, x, h, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = [(y, x)]
    while len(q)>0:
        y1, x1 = q.pop(0)

        for i in range(4):
            nextX = x1 + dx[i]
            nextY = y1 + dy[i]
            if nextY>=0 and nextX>=0 and nextX<w and nextY<h:
                if graph[nextY][nextX]==1:
                    graph[nextY][nextX]=0
                    q.append((nextY, nextX))


T = int(sys.stdin.readline())

for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0]*M for _ in range(N)]
    cnt=0

    for k in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                #dfs(graph, i, j, N, M)
                bfs(graph, i, j, N, M)
                cnt+=1
    print(cnt)


