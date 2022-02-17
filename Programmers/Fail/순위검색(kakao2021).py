#query 순서 언어 and 직무 and 경력 and 음식 점수
def onTheHash(dictionary, words):
    node = dictionary
    for w in words:
        if w == 'chicken' or w == 'pizza':
            if w not in node:
                node[w] = [int(words[4])]
            else:
                node[w].append(int(words[4]))
            break
        
        if w not in node:
            node[w] = {}
            node = node[w]
        else:
            node = node[w]
        
def sorting(dictionary):
    for lang in dictionary:
        node1 = dictionary[lang]
        for job in node1:
            node2 = node1[job]
            for exp in node2:
                node3 = node2[exp]
                for food in node3:
                    node4 = node3[food]
                    node4.sort(reverse=True)

def search(queries, idx, node):
    answer = 0
    if idx==4:
        for i in node:
            if i < int(queries[4]):
                break
            answer+=1
        return answer
    
    if queries[idx]=='-':
        for n in node:
            answer += search(queries, idx+1, node[n])
    else:
        if queries[idx] in node:
            answer += search(queries, idx+1, node[queries[idx]])
    return answer
    

    
def solution(info, query):
    answer = []
    table = [i.split() for i in info]
    queries = [q.replace(' and', '').split() for q in query]
    
    hashing = {}
    for t in table:
        onTheHash(hashing, t)
        
    sorting(hashing)
    
    for q in queries:
        answer.append(search(q, 0, hashing))
    
    return answer
