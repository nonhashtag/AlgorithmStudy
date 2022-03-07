#순열
def permutation(n, m, words):
    if len(words) == m:
        print(" ".join(list(map(str, words))))
        return

    for i in range(1, n+1):
        if i not in words:
            words.append(i)
        else:
            continue
        permutation(n, m, words)
        words.pop()

N, M = map(int, input().split())

permutation(N,M,[])
