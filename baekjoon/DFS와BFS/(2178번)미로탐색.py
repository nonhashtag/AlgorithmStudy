import sys

def bfs(graph, q, visited, h, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while len(q)>0:
        y, x = q.pop(0)

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX>=0 and nextY>=0 and nextX<w and nextY<h:
                if graph[nextY][nextX]=="1" and visited[nextY][nextX]==0:
                    q.append((nextY, nextX))
                    visited[nextY][nextX] = visited[y][x]+1


h, w = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
visited = [[0]*w for _ in range(h)]
visited[0][0] = 1
bfs(graph, [(0,0)], visited, h, w)

print(visited[h-1][w-1])
