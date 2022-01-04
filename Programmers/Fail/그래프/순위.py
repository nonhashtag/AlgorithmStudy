def bfs(idx, win, lose):
    w, l = 0, 0
    vw = [0] * len(win)
    vl = [0] * len(lose)
    wq = [i for i in win[idx]]
    lq = [i for i in lose[idx]]
    while (len(wq) > 0 or len(lq) > 0):
        if len(wq) > 0:
            wc = wq.pop(0)
            vw[wc]=1
            w += 1
            for i in win[wc]:
                if vw[i]==0:
                    wq.append(i)

        if len(lq) > 0:
            lc = lq.pop(0)
            vl[lc]=1
            l += 1
            for i in lose[lc]:
                if vl[i]==0:
                    lq.append(i)

    return w + l


def solution(n, results):
    answer = 0
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for i in results:
        win[i[0]].append(i[1])
        lose[i[1]].append(i[0])

    for i in range(1, n + 1):
        if bfs(i, win, lose) == n-1:
            answer += 1

    print("win : {}".format(win))
    print("lose : {}".format(lose))

    return answer
