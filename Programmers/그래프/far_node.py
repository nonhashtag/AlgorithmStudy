#가장 먼 노드
#dfs로 하면 최단거리 점들이 인접하면 잘못된 값 리턴
def bfs(graph, dist, q):
    arr = []
    cnt=0
    
    while len(q)>0:
        cnt+=1
        for i in q:
            for j in graph[i]:
                if dist[j]==0:
                    arr.append(j)
                    dist[j]=cnt
        q=[]
        while len(arr)>0:
            q.append(arr.pop(0))
                
    
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [0]*(n+1)
    dist[1] = -1
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    #for i in graph:
    #    print(i)
    bfs(graph, dist, [1])
    #print(dist)
    answer = dist.count(max(dist))
    return answer
