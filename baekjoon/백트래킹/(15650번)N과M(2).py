#조합
def combination(cur, n, m, words, answer):
    if len(words)==m:
        answer.append(words.copy())
        return

    for i in range(cur, n+1):
        if i not in words:
            words.append(i)
        else:
            continue
        cur+=1
        combination(cur, n, m, words, answer)
        words.pop()


N, M = map(int, input().split())
answer = []
combination(1, N, M, [], answer)

for i in answer:
    print(" ".join(list(map(str,i))))
