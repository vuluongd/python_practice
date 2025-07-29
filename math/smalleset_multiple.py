from math import log, floor

def smallest_multiple(n):
    primes = []
    for i in range (2, n+1):
        is_prime = True
        for p in primes:
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = 1

    for p in primes:
        max_power = floor(log(n, p))
        result *= p**max_power

    return result

print (f"bội số nhỏ nhất của 20 số nguyên đầu là {smallest_multiple(20)}")