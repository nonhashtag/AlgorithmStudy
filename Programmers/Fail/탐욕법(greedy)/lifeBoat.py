#구명보트 안에 최대 2명의 사람이 들어간다.
#people에는 사람 몸무게 리스트가 매개변수로 ex)[10,30,50]
#limit에는 구명보트에 최대 실을 수 있는 무게 ex)100
#모든 사람을 실을 수 있는 보트의 최소 갯수를 구하시오. ex답안) 2개
def loadwith(limit: int, people:list)->int:
    if len(people)==1:
        return -1
    if len(people)==2:
            return 1 if people[0]+people[1]<=limit else -1

    man=people[0]
    start, last = 1, len(people)
    effort=-1
    while True:
        middle=(start+last)//2
        if start==middle:
            return effort
        if people[middle]+man < limit:
            last=middle
            if people[effort]<=people[middle]:
                effort=middle
        elif people[middle]+man==limit:
            return middle
        else:
            start=middle

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while len(people)>0:
        other = loadwith(limit, people)
        if other!=-1:
            del people[other]
        del people[0]
        answer+=1
        
    return answer
