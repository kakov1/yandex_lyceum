def eratosthenes(n):
    primes = list(range(3, n + 1))
    i = 2
    deleted = []
    while True:
        count = 0
        prev = primes[:]
        for prime in primes:
            if not prime % i and prime != i:
                deleted.append(prime)
                del primes[count]
            count += 1
        if prev == primes:
            print(*deleted)
            break
        for prime in primes:
            if prime > i:
                i = prime
                break
