def solution(n, times):
    answer = max(times)*n
    s, e = 1, max(times)*n
    m = (s+e)//2

    while s<e:
        done = sum(m//t for t in times)
        if done>=n:
            answer=min(answer, m)
            e=m
            m=(s+e)//2
        else:
            s=m+1
            m=(s+e)//2

    return answer
