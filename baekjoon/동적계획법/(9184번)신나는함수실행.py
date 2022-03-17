import sys

def func(arr):
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i==0 or j==0 or k==0:
                    arr[i][j][k]=1
                elif i<j and j<k:
                    arr[i][j][k] = arr[i][j][k-1] + arr[i][j-1][k-1] - arr[i][j-1][k]
                else:
                    arr[i][j][k] = arr[i-1][j][k] + arr[i-1][j-1][k] + arr[i-1][j][k-1] - arr[i-1][j-1][k-1]


arr = [[[0]*21 for _ in range(21)] for _ in range(21)]
func(arr)

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break

    print(f"w({a}, {b}, {c}) =", end=" ")
    if a<=0 or b<=0 or c<=0:
        print(arr[0][0][0])
        continue
    elif a > 20 or b > 20 or c > 20:
        print(arr[20][20][20])
        continue
    print(arr[a][b][c])
