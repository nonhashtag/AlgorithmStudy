def solution(citations):
    answer = 0
    while True:
        makeshift = [i for i in citations if i>=answer]
        if len(makeshift) <= answer:
            answer=len(makeshift)
            break
        answer += 1
    return answer

print(solution([3,0,5,6,1,5]))
