#전역변수를 이용하면, 함수만으로 처리 가능하다.
def blue(arr, start, length):
    answer = 0
    check = True
    if length==1 and arr[start[0]][start[1]]==0:
        return 0

    for i in range(start[0], start[0]+length):
        for j in range(start[1], start[1]+length):
            if arr[i][j]==0:
                check = False
                break
        if not check:
            break

    if check:
        return 1
    else:
        answer += blue(arr, (start[0], start[1]), length//2)
        answer += blue(arr, (start[0], start[1]+length//2), length//2)
        answer += blue(arr, (start[0]+length//2, start[1]), length//2)
        answer += blue(arr, (start[0]+length//2, start[1]+length//2), length//2)

    return answer

def white(arr, start, length):
    answer = 0
    check = True
    if length==1 and arr[start[0]][start[1]]==1:
        return 0

    for i in range(start[0], start[0]+length):
        for j in range(start[1], start[1]+length):
            if arr[i][j]==1:
                check = False
                break
        if not check:
            break

    if check:
        return 1
    else:
        answer += white(arr, (start[0], start[1]), length//2)
        answer += white(arr, (start[0], start[1]+length//2), length//2)
        answer += white(arr, (start[0]+length//2, start[1]), length//2)
        answer += white(arr, (start[0]+length//2, start[1]+length//2), length//2)

    return answer



N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

print(white(arr, (0, 0), N))
print(blue(arr, (0, 0), N))
