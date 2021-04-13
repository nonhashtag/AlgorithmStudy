def solution(name):
    answer = 0
    AtoN=[i for i in range(65,79)]
    MtoZ=list(reversed([i for i in range(79,91)]))
    
    if name=="A":
        return 0
    
    if len(name)>=2:
        for i in range(1, len(name)):
            if name[i]=="A":
                answer-=1
            else:
                break
            
    for i in name:
        if ord(i) in AtoN:
            answer += ord(i)-65
        elif ord(i) in MtoZ:
            answer += MtoZ.index(ord(i))+1
    
    return answer+len(name)-1
