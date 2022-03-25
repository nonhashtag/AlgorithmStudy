import sys

def isPrime(N):
    if N==1:
        return 0
    if N==2:
        return 1
    elif N==3:
        return 1
    for i in range(2, int(N**0.5)+2):
        if N % i == 0:
            return 0
    return 1

def primes(arr, N):
    for i in range(1, N+1):
        if isPrime(i)==1:
            arr.append(i)

def search(arr, N):
    start, end = 0, 0
    answer=0
    summary = arr[start]
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
arr = []
primes(arr, N)
print(search(arr, N))
