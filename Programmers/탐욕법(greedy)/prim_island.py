def prim(edge: list, node: list, start: int):
    selected=[]
    V = [start]
    while len(V)!=len(node):
        for i in edge:
            if (i[0] in V) and (i[1] not in V):
                V.append(i[1])
                selected.append(i[2])
                break
            elif (i[0] not in V) and (i[1] in V):
                V.append(i[0])
                selected.append(i[2])
                break
    return sum(selected)
    
            
    

    
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    islands = sorted(list(set([j for i in costs for j in i[:2]])))
    start = costs[0][0]
    answer = prim(costs, islands, start)
    print(islands)
    
    
    return answer


#a=[[1,2,3,4,5],[10,29,394,959]]
#print([1,2,3,4,5] in a)
