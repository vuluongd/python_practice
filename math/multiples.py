# tổng các chữ số dưới 1000 là bộ số của 3 và 5

total = 0

for i in range (0,1000):
    if i%3 == 0 or i%5==0:
        total+=i

print (f"tổng các chữ số dưới 1000 là bội số của 3 và 5 là: {total}")