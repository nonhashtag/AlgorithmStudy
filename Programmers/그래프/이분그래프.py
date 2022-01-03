N, M = map(int, input().split()) #크기선정
myGraph = [[] for i in range(N+1)]
divided = [0]*(N+1)    #그룹을 1과 -1로 나눌 배열

def dfs(myGraph, divided, vert, group):
    divided[vert] = group

    for i in myGraph[vert]:
        if divided[i]==divided[vert]:  #연결되어 있는데 같은 그룹이라면??
            return False
        if divided[i]!=0:   #사실상 0일 때와 elif를 써서 조건문을 쓰는게 더 효율적이다.
            continue
        if dfs(myGraph, divided, i, -group) is False:  #다음 점을 돌려봤는데 false라면?
            return False
    return True

for i in range(M):
    a, b = map(int, input().split())
    myGraph[a].append(b)
    myGraph[b].append(a)

#dfs(myGraph, divided, 1, 1)

#print(myGraph)
print("YES" if dfs(myGraph, divided, 1, 1)==True else "NO")
