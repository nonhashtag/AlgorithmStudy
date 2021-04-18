#구명보트 안에 최대 2명의 사람이 들어간다.
#people에는 사람 몸무게 리스트가 매개변수로 ex)[10,30,50]
#limit에는 구명보트에 최대 실을 수 있는 무게 ex)100
#모든 사람을 실을 수 있는 보트의 최소 갯수를 구하시오. ex답안) 2개
def solution(people, limit):
    answer = 0
    people.sort()
    first, last = 0, len(people)-1
    while first<=last:
        answer+=1
        if people[first]+people[last]<=limit:
            first+=1
        last-=1

    return answer
