N = int(input())
cnt = 0
number = 666
while True:
    if "666" in str(number):
        cnt+=1
    if cnt==N:
        break
    else:
        number+=1

print(number)