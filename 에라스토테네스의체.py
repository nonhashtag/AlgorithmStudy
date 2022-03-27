# 에라스토테네스의 체
def prime_list(n):
    sieve = [True]*(n+1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i]==True:
            for j in range(i*i, n+1, i):
                sieve[j]=False
    return [i for i in range(2, N+1) if sieve[i]==True]
  
  
  print(prime_list(100))
