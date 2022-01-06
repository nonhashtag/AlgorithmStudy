def getResult(current, n, result, answer):
    if(current>=n):
        #프린트할지, 정답 리스트를 따로 생성해서 추가할지는 알아서 하도록하고
        answer.append(result[:])
        print(result)
    else:
        for i in range(1, n+1):
            if i not in result:
                result[current]=i
                getResult(current+1, n, result, answer)
                result[current] = 0


n=3
result=[0]*n
answer=[]
getResult(0, n, result, answer)
print("######")
for i in answer:
    print(i)
