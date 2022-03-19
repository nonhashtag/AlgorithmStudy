def angle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else:
        return False

while True:
    A, B, C = map(int, input().split())
    if A+B+C==0:
        break
    if angle(A,B,C):
        print("right")
    else:
        print("wrong")
