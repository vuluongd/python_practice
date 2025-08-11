import numpy as np

start_arr = np.array([[0, 0, 0],
                     [1, 1, 1]]) 

end_arr = np.array([[2, 2, 2],
                    [3, 3, 3]])

diff = start_arr[:, None, :] - end_arr[None,:, :]

print(diff.shape) 
print(diff)