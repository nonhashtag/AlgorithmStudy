#Stack
def pair(b):
    if b=='(':
        return ')'
    elif b=='[':
        return ']'
    elif b=='{':
        return '}'

def validation(_input):
    stack = []
    top = -1
    for i in _input:
        if top == -1:
            stack.append(i)
            top+=1
        else:
            if i == pair(stack[top]):
                stack.pop(top)
                top-=1
            else:
                stack.append(i)
                top+=1
        #print(stack)
        
    return 1 if len(stack)==0 else 0
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[0]
        answer+=validation(s)
    
    
    return answer
