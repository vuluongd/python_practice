def f(x):
    return x**2
def trapezoid_integral(f, a,b,n):
    h = (b-a)/n
    result = 0.5* (f(a)+f(b))
    for i in range(1,n):
        result += f(a + i*h)
    return result*h

a = 0
b = 2
n = 1000

result = trapezoid_integral(f,a,b,n)

print (result)


