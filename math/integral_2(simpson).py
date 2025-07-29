def f(x):
    return x**2
def simpson_integral(f, a, b, n):
    if n%2 == 1:
        n+=1
    h = (b-a)/n
    result = f(a)+f(b)

    for i in range (1,n,2):
        result += 4*f(a+i*h)
    for i in range (2, n-1,2):
        result += 2*f(a+i*h)
    
    return result * h/3

a = 0
b = 2
n = 1000

result_simpson = simpson_integral(f, a, b, n)

print (f"result_simpson: {result_simpson}")


