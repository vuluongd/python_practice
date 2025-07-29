def largest_prime_factor(n):
    i = 2
    while i * i<=n:
        if n%i == 0:
            n //=i
        else:
            i += 1
            
    return n

num = 600851475143
result = largest_prime_factor(num)

print(f"Ước chung lớn nhất của {num} là {result}")