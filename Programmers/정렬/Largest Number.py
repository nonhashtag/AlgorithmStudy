#시간초과하는 문제가 있다.
from itertools import permutations

def solution(numbers):
    permute = list(permutations(numbers, len(numbers)))
    joined = [''.join(map(str,i)) for i in permute]
    
    return str(max([int(i) for i in joined]))
