def dfs(graph, score, visit, root, cur):
    visit[cur] = 1
    if root!=cur:
        score[root][0]+=1
        score[cur][1]+=1
    for i in graph[cur]:
        if visit[i]==0:
            dfs(graph, score, visit, root, i)


def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    score = dict()

    for i,j in results:
        graph[i].append(j)

    for i in range(1,n+1):
        score.setdefault(i,[0,0])

    for i in range(1, n+1):
        dfs(graph, score, [0]*(n+1), i, i)

    for i in score:
        if sum(score[i])==n-1:
            answer+=1

    return answer
