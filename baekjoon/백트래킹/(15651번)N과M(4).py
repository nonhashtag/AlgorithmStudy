#중복조합
import sys

def combination_dup(n, m, cur, words, answer):
    if len(words)==m:
        answer.append(words.copy())
        return

    for i in range(cur,n+1):
        words.append(str(i))
        combination_dup(n, m, cur, words, answer)
        cur += 1
        words.pop()

N, M = map(int, sys.stdin.readline().split())
answer = []

combination_dup(N, M, 1, [], answer)
for i in answer:
    print(" ".join(i))