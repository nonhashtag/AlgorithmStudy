#stack 사용
def solution(s):
    top = -1
    stack = []
    if len(s)==1:
        return 0
    for i in s:
        if len(stack)==0:
            stack.append(i)
            top+=1
        else:
            if stack[top]==i:
                stack.pop(top)
                top-=1
            else:
                stack.append(i)
                top+=1
    return 1 if len(stack)==0 else 0
