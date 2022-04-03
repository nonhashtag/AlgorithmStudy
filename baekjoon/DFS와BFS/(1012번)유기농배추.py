import sys

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
                dfs(graph, i, j, N, M)
                cnt+=1
    print(cnt)


