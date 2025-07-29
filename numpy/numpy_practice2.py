import numpy as np

danh_sach = [[1,2,3],[2,4,6],[3,5,8]];

ma_tran_1 = np.array(danh_sach)

print(ma_tran_1)

ma_tran_2 = np.ones((3,3))

print(ma_tran_2)

ma_tran_3 = np.zeros((2,2))

print(ma_tran_3)

ma_tran_don_vi = np.eye(4,4)
print(ma_tran_don_vi)

ma_tran_5 = np.arange(1,10).reshape(3,3)
print(ma_tran_5)

phan_tu = ma_tran_5[1,2] #lấy phần tử hàng 1 cột 2
print(phan_tu)

print(np.dot(ma_tran_1,ma_tran_5))
