def dfs(graph, visited, cur):
    visited[cur] = 1
    print(cur, end=" ")

    for i in graph[cur]:
        if visited[i]==0:
            dfs(graph, visited, i)

def bfs(graph, visited, q):
    visited[q[0]]=1
    while len(q)>0:
        cur = q.pop(0)
        print(cur, end=" ")

        for i in graph[cur]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1


vert, edge, node = map(int, input().split())
graph = [[] for _ in range(vert+1)]
visited = [0]*(vert+1)

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(graph, visited, node)
visited = [0]*(vert+1)
print()
bfs(graph, visited, [node])
