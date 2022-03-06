def hanoi(n, a, b):
    if n==1:
        print(f"{a} {b}")
    else:
        temp = 6-a-b
        hanoi(n-1, a, temp)
        print(f"{a} {b}")
        hanoi(n - 1, temp, b)



K = int(input())
print(2**K-1)
hanoi(K, 1, 3)
