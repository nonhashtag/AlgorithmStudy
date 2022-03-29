import sys

arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90

for i in range(11, 101):
    arr[i] = arr[i-2] + arr[i-3]

for t in range(int(sys.stdin.readline())):
    N = int(int(sys.stdin.readline()))
    print(arr[N])
