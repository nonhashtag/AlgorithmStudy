import sys

def euclidean(x1, y1, x2, y2):
    return ( (abs(x1-x2))**2 + (abs(y1-y2))**2 )**0.5

N = int(sys.stdin.readline())
# 리스트 입력값 x1, y1, r1, x2, y2, r2
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = []
for x1, y1, r1, x2, y2, r2 in arr:
    t_dist = euclidean(x1, y1, x2, y2)
    if t_dist==0:
        if r1==r2:
            answer.append(-1); continue
        else:
            answer.append(0); continue

    if t_dist > r1+r2:
        answer.append(0)
    elif t_dist == r1+r2 or t_dist==abs(r1-r2):
        answer.append(1)
    elif t_dist < r1+r2:
        if t_dist > abs(r1-r2):
            answer.append(2)
        elif t_dist == abs(r1-r2):
            answer.append(1)
        else:
            answer.append(0)

for i in answer:
    print(i)
