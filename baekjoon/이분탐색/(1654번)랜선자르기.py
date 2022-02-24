K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))
arr.sort()
answer=0
start, end = 1, max(arr)

while start<=end:
    #mid가 작을 수로 temp가 커진다.
    mid = (start + end)//2
    temp = sum(i//mid for i in arr if mid > 0)
    #mid가 너무 크다
    if temp < N:
        end = mid-1

    #mid가 너무 작다
    else:
        start = mid+1


mid = (start+end)//2

print(mid)
