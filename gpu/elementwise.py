# Use OpenCL To Add Two Random Arrays (Using PyOpenCL Arrays and Elementwise)
import numpy as np
import pyopencl as cl
import pyopencl.array as cl_array

# Create a context and command queue
context = cl.create_some_context()
queue = cl.CommandQueue(context)
# Generate two random arrays
a_np = np.random.rand(50000).astype(np.float32)
b_np = np.random.rand(50000).astype(np.float32)
# Transfer the arrays to the device
a_g = cl_array.to_device(queue, a_np)
b_g = cl_array.to_device(queue, b_np)
# Create an empty array for the result
res_g = cl_array.empty_like(a_g)
# Use Elementwise to add the arrays on the device
sum = cl_array.elementwise.ElementwiseKernel(context, "float *x, float *y, float *z", "z[i] = x[i] + y[i]", "sum")
sum(a_g, b_g, res_g)
# Transfer the result back to the host
res_np = res_g.get()
# Verify the result
print (np.allclose(res_np, a_np + b_np))  # Should print True
print(res_np)  # Print the resulting array
print(a_np)
print(b_np)
