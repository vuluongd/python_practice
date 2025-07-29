#tổng các chữ số chẵn nhỏ hơn 4 triệu trong dãy fibobacci 
a, b = 1,2
total = 0

while b < 4*10**6:
    if b%2 == 0:
        total +=b

    a, b = b, a+b
print (f"tổng các chữ số chẵn nhỏ hơn 4 triệu trong dãy fibobacci: {total}")

