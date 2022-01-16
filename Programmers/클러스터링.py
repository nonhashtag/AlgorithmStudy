def filt(string):
    arr = []
    string = string.upper()
    for i in range(len(string)-1):
        if ((65<=ord(string[i]) and ord(string[i])<=90)
        and (65<=ord(string[i+1]) and ord(string[i+1])<=90)):
            arr.append(string[i]+string[i+1])
    return arr

def bind(string):
    answer = []
    if len(string)<=1:
        return []
    for i in range(len(string)-1):
        answer.append(string[i]+string[i+1])
    return answer

def solution(str1, str2):
    str_1 = {}
    str_2 = {}
    print(filt(str1))
    print(filt(str2))
    for i in filt(str1):
        if i in str_1:
            str_1[i]+=1
        else:
                str_1[i]=1
    for i in filt(str2):
        if i in str_2:
            str_2[i]+=1
        else:
            str_2[i]=1
    
    inner = 0
    outer = 0
    for i in str_1:
        if i in str_2:
            if str_1[i]==str_2[i]:
                inner+=str_1[i]
                outer-=str_1[i]
            else:
                inner+=min(str_1[i], str_2[i])
                outer-=min(str_1[i], str_2[i])
        outer+=str_1[i]
    for i in str_2:
        outer+=str_2[i]

    
    return int(65536*(inner/outer)) if outer!=0 else 65536
