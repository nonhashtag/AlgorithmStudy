import sys

# 에라스토테네스의 체
def prime_list(n):
    sieve = [True]*(n+1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i]==True:
            for j in range(i*i, n+1, i):
                sieve[j]=False
    return [i for i in range(2, N+1) if sieve[i]==True]

def search(arr, N):
    start, end = 0, 0
    answer=0
    summary = arr[start] if len(arr)>0 else 0
    while end<len(arr):
        if summary<N:
            end+=1
            if end<len(arr):
                summary += arr[end]
        elif N<summary:
            summary -= arr[start]
            start+=1
        else:
            answer+=1
            end+=1
            if end<len(arr):
                summary += arr[end]
    return answer

N = int(sys.stdin.readline())
arr = prime_list(N)

print(search(arr, N))
