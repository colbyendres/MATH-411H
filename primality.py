from math import sqrt
import random 
import time

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
    primes = [2**19-1, 2**31-1, 2**31-1, 2**61-1]
    digits = [len(str(p)) for p in primes]
    times = len(primes) * [0]
    k = 8
    trials = 4

    for t in range(trials):
        for i,p in enumerate(primes):
            start = time.time()
            millerRabin(p, k)
            stop = time.time()
            times[i] += stop - start

    print([t / trials for t in times])    

stress2()

# Trial Division
# [0.03783106803894043, 180.85682368278503, 179.10301184654236, > 1hr]
# [0.03332996368408203, 172.12513613700867, 171.46160888671875, > 1hr]
# [0.03556, 176.45, 175.28, > 1hr]

# Fast Trial Division
# [2.7894973754882812e-05, 0.002130270004272461, 0.002077817916870117, 65.28326511383057]
# [2.8133392333984375e-05, 0.002103090286254883, 0.002053976058959961, 65.70097780227661]
# [0.000028, 0.00211, 0.00206, 65.492]

# Fermat 
# [2.950429916381836e-05, 7.772445678710938e-05, 7.611513137817383e-05, 0.00015437602996826172]

# Miller-Rabin
# [3.248453140258789e-05, 8.469820022583008e-05, 8.308887481689453e-05, 0.00016319751739501953]
