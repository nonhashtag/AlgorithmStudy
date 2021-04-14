def solution(name):
    loc=0
    AtoZ = [min(ord(i)-ord("A"), (ord("Z")-ord(i))+1) for i in name]
    
    answer=sum(AtoZ)
    while True:
        AtoZ[loc]=0
        if sum(AtoZ)==0:
            return answer
        left, right = 1, 1
        while AtoZ[loc-left]==0:
            left+=1
        while AtoZ[loc+right]==0:
            right+=1
        answer+= left if left<right else right
        loc+= -left if left<right else right
        
        
print(solution("BBAAAAAB"))
