from math import sqrt
import random 

def trial_division(n):
    if n < 2:
        return False
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

def fast_trial_division(n):
    if n <= 3:
        return n >= 2 # prime iff n = 2 or 3
    if n % 6 != 1 and n % 6 != 5:
        return False # all primes > 3 are +/- 1 mod 6
    stop = 1+int(sqrt(n))
    for d in range(3,stop,2):
        if n % d == 0:
            return False
    return True

def fermat(n, k):
    if n <= 3:
        return n >= 2 # prime iff n = 2 or 3
    if n % 6 != 1 and n % 6 != 5:
        return False # all primes > 3 are +/- 1 mod 6
    for i in range(k):
        a = random.randint(2,n-1)
        if pow(a,n-1,n) != 1:
            return False
    return True

def millerRabin(n, k):
    if n <= 3:
        return n >= 2 # prime iff n = 2 or 3
    if n % 6 != 1 and n % 6 != 5:
        return False # all primes > 3 are +/- 1 mod 6
    s = (n-1) & ~(n-1)                           # bit twiddle hack
    d = (n-1) >> s 
    for i in range(k):
        a = random.randint(2,n-1)
        x = pow(a,d,n)
        if x == 1:                               # a^d = 1 mod n, strong probable prime
            continue
        for j in range(s):                       # Check second condition
            y = (x * x) % n                      # Compute x^{d2^k} mod n
            if y == 1 and x != 1 and x != n-1:   # x is a nontrivial sqrt => n composite
                return False
            x = y                                # Fast squaring
        if x != 1:                               # Fermat test
            return False
    return True

def stress1():
    start = 10 ** 5
    stop = 10 ** 6
    k = 5
    # trial = [fast_trial_division(i) for i in range(start, stop)]
    # ferm = [fermat(i,k) for i in range(start, stop)]
    # MR = [millerRabin(i,k) for i in range(start, stop)]

    # for i in range(start, stop):
    #     if trial[i-start] ^ ferm[i-start]:
    #         print('i=',i,'Fermat:',ferm[i-start])
    #     if trial[i-start] ^ MR[i-start]:
    #         print('i=',i,'MR:',MR[i-start])

def stress2():
    BIG_PRIME = 2 ** 127 - 1
    print(fast_trial_division(BIG_PRIME))
    # print(fermat(BIG_PRIME+1,10))

stress2()