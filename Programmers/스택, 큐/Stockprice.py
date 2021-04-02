def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(0)
    for i in range(len(prices)):
        if i == len(prices) - 1:
            break
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:

                answer[i] += 1
                break
            else:
                answer[i] += 1

    return answer


test = [1, 2, 3, 2, 3]
print(solution(test))

ans=[0]*3
print(ans)
