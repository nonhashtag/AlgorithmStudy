# 좀더 간단하게 풀 수 있을 듯 하다.
def counting(arr, n):
    s, e = 0, len(arr)
    idx = 0
    while True:
        if s>=e:
            idx=e; break
        m = (s+e)//2
        if arr[m]==n:
            idx=m
            while idx>0:
                idx-=1
                if arr[idx]<n:
                    idx+=1
                    break
            break

        elif arr[m]<n:
            s = m+1
        else:
            e = m
    return len(arr)-idx

def onTheHash(hashing, info):
    for i in info:
        key = ''.join(i.split()[:4])
        if key not in hashing:
            hashing[key] = [int(i.split()[4])]
        else:
            hashing[key].append(int(i.split()[4]))

    for i in hashing:
        hashing[i].sort()


def search(hashing, query):
    answer = 0
    required = []

    for h in hashing:
        if all(q in h for q in query[:-1]):
            answer+=counting(hashing[h], int(query[-1]))

    return answer


def solution(info, query):
    answer = []
    queries = [q.replace(' and ', ' ').replace('-', '').split() for q in query]

    hashing = {}
    onTheHash(hashing, info)
    for q in queries:
        answer.append(search(hashing, q))


    return answer
