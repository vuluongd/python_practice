import numpy as np

arr = np.arange(1,26).reshape(5,5)
print ("ma tran goc: ", arr)

tinh_tong_duong_cheo_chinh = np.trace(arr)
print (tinh_tong_duong_cheo_chinh)

chuyen_vi = arr.transpose()
print(chuyen_vi)

det = np.linalg.det(arr)
print(det)
