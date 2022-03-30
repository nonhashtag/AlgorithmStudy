import sys

def dfs(graph, cur, visited):
    visited[cur]=1

    for i in graph[cur]:
        if visited[i]==0:
            dfs(graph, i, visited)

verts = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
graph = [[] for _ in range(verts+1)]
visited = [0] * (verts+1)

for i in range(edges):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
answer = 0
for i in visited:
    if i==1:
        answer+=1

print(answer-1)
