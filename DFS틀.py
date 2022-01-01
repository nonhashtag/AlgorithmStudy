# graph = 그래프
# x = 최초 노드(현재 방문 노드)
# visited = 방문한 노드들의 리스트(bool 타입 혹은 0,1 등의 범주화 가능)
def DFS(graph, x, visited: list):
    visited[x] = True

    for i in range(len(graph)):
        y = graph[x][i]
        if visited[y] == False:
            DFS(graph, y, visited)
