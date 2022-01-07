def solution(s):
    idx = 0
    sen = list(s)
    #print(sen)
    while (idx < len(sen)-1):
        if sen[idx] == sen[idx+1]:
            del sen[idx]
            del sen[idx]
            if idx>0:
                idx-=1
        else:
            idx+=1
        
        #if (idx==len(sen)):
        #    idx=0
    
    
    return 1 if len(sen)==0 else 0
