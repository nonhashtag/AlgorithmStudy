def dfs(graph, cur, target, summ):
    if cur == len(graph):
        if summ == target:
            return 1
        else:
            return 0

    answer = 0

    answer += dfs(graph, cur + 1, target, summ + graph[cur])
    answer += dfs(graph, cur + 1, target, summ - graph[cur])
    return answer


def solution(numbers, target):
    answer = dfs(numbers, 0, target, 0)

    return answer
