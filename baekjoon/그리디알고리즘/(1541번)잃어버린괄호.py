arr = input().replace("-", " - ").replace("+", " ").split()
idx = 0
sign = False
answer=0

while idx<len(arr):
    if sign==False:
        if arr[idx] == "-":
            sign=True
        else:
            answer += int(arr[idx])
        idx+=1
    else:
        if arr[idx] != "-":
            answer -= int(arr[idx])
        idx+=1

#print(arr)
print(answer)
