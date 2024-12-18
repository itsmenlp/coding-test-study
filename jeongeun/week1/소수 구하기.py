import math

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return sieve

def print_primes_in_range(M, N):
    sieve = sieve_of_eratosthenes(N)
    
    for i in range(M, N + 1):
        if sieve[i]:
            print(i)

M, N = map(int, input().split())

print_primes_in_range(M, N)
