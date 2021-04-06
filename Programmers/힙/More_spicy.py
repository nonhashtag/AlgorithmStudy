def solution(scoville, K):
    answer = 0
    arr= scoville
    while len(arr) >= 2:
        if all(i>=K for i in arr):
            break
        arr.sort(reverse=True)
        arr[1]=arr[0] + 2*arr[1]
        del(arr[0])
        answer+=1
            
    #실패시 -1리턴
    if any(i<K for i in arr):
        return -1
    return answer
