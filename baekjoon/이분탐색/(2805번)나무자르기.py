N, M = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 1, max(trees)

while s <= e:
    m = (s+e)//2
    #길이를 길게 잡으면, 가져가는게 적어짐
    got = sum(i-m for i in trees if i>m)

    #길이가 아직 짧다
    if M <= got:
        s = m+1
    #길이가 아직 짧다
    else:
        e = m-1

m = (s+e)//2
print(m)
