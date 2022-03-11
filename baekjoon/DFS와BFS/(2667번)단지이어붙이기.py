import sys
# DFS와 BFS 방식 모두 구현


def dfs(graph, y, x, cnt):
    if graph[y][x]=="1":
        cnt+=1
        graph[y][x] = "0"
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nextY = y+dy[i]
            nextX = x+dx[i]

            if 0<=nextX and nextX<=len(graph)-1 and 0<=nextY and nextY<=len(graph)-1:
                cnt = dfs(graph, nextY, nextX, cnt)

    return cnt

def bfs(graph, y, x, cnt):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    graph[y][x]="0"
    cnt+=1
    q = [(y,x)]
    while len(q)>0:
        ny, nx = q.pop(0)
        for i in range(4):
            nextX = nx+dx[i]
            nextY = ny+dy[i]
            if 0<=nextX and 0<=nextY and nextX<=len(graph)-1 and nextY<=len(graph)-1:
                if graph[nextY][nextX]=="1":
                    graph[nextY][nextX]="0"
                    cnt+=1
                    q.append((nextY, nextX))
    return cnt






N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))

answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j]=="1":
            answer.append(bfs(graph, i, j, 0))
            #answer.append(dfs(graph, i, j, 0))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
