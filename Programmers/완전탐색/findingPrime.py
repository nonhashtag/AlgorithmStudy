from itertools import permutations

#튜플타입의 숫자조합을 정수타입으로 변환
def invert(tuples) -> int:
    arr = list(tuples)
    num = ''.join(arr)
    return int(num)

#소수인지 판단
def prime(num):
    if num<=2:
        if num==2:
            return num
        else:
            return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
        elif i * i > num:
            return num


def solution(numbers):
    #answer = 0
    primes = [invert(i) for n in range(1,len(numbers)+1) for i in permutations(numbers, n) if prime(invert(i)) != 0]
    #answer = len(set(primes))
    print(primes)
    return len(set(primes))


print(solution("011"))
