#숫자가 걍 10의 배수면 0, 아니면 1을 리턴하는 게임이다...
def game(n):
    return 1 if n%10==0 else 0

T = int(input())
N = []
for i in range(T):
    N.append(int(input()))

for i in N:
    print(game(i))
