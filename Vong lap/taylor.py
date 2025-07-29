#pp lặp taylor
n = int(input("nhap_n: "))
x = float(input("nhap_x: "))

S =1.0
factorial = 1
x_power = 1

for i in range(1,n+1):
    factorial = factorial*i
    x_power = x_power*x
    S = S + x_power/factorial

print(S)


