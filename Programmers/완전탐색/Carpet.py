def solution(brown, yellow):
    perimeter = brown + 4
    area = brown + yellow
    
    for i in range(3, int(perimeter/2)):
        if area%i==0 and (2*i)+2*(area/i)==perimeter:
            return [int(area/i), i]
