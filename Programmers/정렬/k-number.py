def solution(array, commands):
    answer = []
    for i in commands:
        makeshift=[]
        makeshift=array[i[0]-1:i[1]]
        makeshift.sort()
        answer.append(makeshift[i[2]-1])
    return answer
