import pyopencl as cl
import numpy as np

N = 10
a = np.arange(N).astype(np.float32)
b = np.arange(N).astype(np.float32)
c = np.empty_like(a)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
c_buf = cl.Buffer(ctx, mf.WRITE_ONLY, c.nbytes)

kernel_code = """
__kernel void vector_add(__global const float* A,
                         __global const float* B,
                         __global float* C) {
    int i = get_global_id(0);
    C[i] = A[i] + B[i];
}
"""

program = cl.Program(ctx, kernel_code).build()

program.vector_add(queue, a.shape, None, a_buf, b_buf, c_buf)

cl.enqueue_copy(queue, c, c_buf)

print("A:", a)
print("B:", b)
print("C = A + B:", c)