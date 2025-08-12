"""
Pandas Basic Operations Practice

Bài tập:
1. Tạo một Series từ:
   a) list [10, 20, 30, 40]
   b) numpy array np.arange(5)
   c) dict {"a":1, "b":2, "c":3}

2. Tạo DataFrame bằng cách kết hợp các Series trên.

3. Xem thông tin DataFrame:
   - Kích thước (.shape)
   - Kiểu dữ liệu (.dtypes)
   - Thống kê mô tả (.describe())

4. Truy xuất dữ liệu:
   - Dòng đầu tiên bằng .iloc
   - Cột 'B' bằng .loc
   - Giá trị ở hàng 2, cột 'C' bằng .at

5. Thêm một cột mới = cột 'A' * 10.

6. Xóa cột 'B'.
"""
import pandas as pd
import numpy as np

#tạo series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series(np.arange(5))
s3 = pd.Series({"a":1, "b":2, "c":3})

print(s1)
print(s2)
print(s3)

#tạo dataframe
df = pd.DataFrame({
    "A":s1,
    "B":s2,
    "C":s3
})

print(df)
#thêm mô tả 
print("\nKích thước DataFrame:", df.shape)

print("\nKiểu dữ liệu:")
print(df.dtypes)

print("\nThống kê mô tả:")
print(df.describe())

#truy xuất dữ liệu
print("Dòng đẩu tiên: ")
print(df.iloc)

print("Cột B: ")
print(df.loc[:, "B"])

print("Giá trị hàng 2 cột C: ")
print(df.at[1, "C"])


# 5. Thêm cột mới
df["A_times_10"] = df["A"] * 10
print("DataFrame sau khi thêm cột A_times_10:")
print(df)

# 6. Xóa cột B
df = df.drop(columns=["B"])
print("DataFrame sau khi xóa cột B:")
print(df)