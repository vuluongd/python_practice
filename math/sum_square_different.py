sum1 = 0
sum2 = 0

for i in range(1,101):
    sum1 += i
    sum2 += i*i

square_of_sum = sum1*sum1
sum_square = sum2

result = square_of_sum-sum_square

print (f"sự khác biệt giữa bình phương của tổng 100 số đầu tiên và tổng bình phương 100 số đầu tiên là {result}")