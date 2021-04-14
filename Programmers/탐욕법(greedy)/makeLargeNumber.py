def solution(number, k):
    numbers=list(map(int,number))
    idx=0
    if len(numbers)==1:
        return number
    while k>0 and idx<len(numbers):
        if idx==len(numbers)-1:
            for i in range(k):
                del numbers[-1]
            k-=k
            break
        if numbers[idx] < numbers[idx+1]:
            del numbers[idx]
            k-=1
            if idx>0:
                idx-=1
        else:
            idx+=1
    numbers=list(map(str,numbers))
    return ''.join(numbers)
  
  print(solution("12312",2))
