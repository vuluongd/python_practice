def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

count = 0
num = 1
while (num < 2*10**6):
    if is_prime(num):
        count += num

    num += 1

print(f"result: {count}")
        