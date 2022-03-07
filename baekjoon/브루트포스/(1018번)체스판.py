def matching(arr, row, col):
    w_cnt=0
    b_cnt=0
    w_arr = [['W','B']*4 if i%2==0 else ['B','W']*4 for i in range(8)]
    b_arr = [['B','W']*4 if i%2==0 else ['W','B']*4 for i in range(8)]

    for i in range(row, row+8):
        for j in range(col, col+8):
            if w_arr[i-row][j-col] != arr[i][j]:
                w_cnt+=1
            if b_arr[i-row][j-col] != arr[i][j]:
                b_cnt+=1

    return min(w_cnt, b_cnt)


N, M = map(int, input().split())
arr= []
for i in range(N):
    arr.append(list(input()))


answer = N*M
for i in range(N-7):
    for j in range(M-7):
        answer = min(answer, matching(arr, i, j))
print(answer)
