#구명보트 안에 최대 2명의 사람이 들어간다.
#people에는 사람 몸무게 리스트가 매개변수로 ex)[10,30,50]
#limit에는 구명보트에 최대 실을 수 있는 무게 ex)100
#모든 사람을 실을 수 있는 보트의 최소 갯수를 구하시오. ex답안) 2개
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    boat=[]
    idx=0
    while len(people)>0:
        boat.append([people.pop(0)])
        other = [people.index(man) for man in people if man+boat[idx][0]<=limit]
        if len(other)>0:
            boat[idx].append(people.pop(other[0]))
        if len(people)==0:
            break
        idx+=1
    answer = len(boat)
        
    return answer

