import sys

def search(arr, n):
    start, end = 0, 0
    if sum(arr)<n:
        return 0
    answer = len(arr)
    summary = arr[start]
    while end<=len(arr):
        if summary < n:
            end+=1
            if end < len(arr):
                summary+=arr[end]
        else:
            answer = min(answer, end-start+1)
            summary-=arr[start]
            start+=1
            if answer==1:
                break
    return answer

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(search(arr, K))
