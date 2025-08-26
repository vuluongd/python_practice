import pyopencl as cl
import numpy as np

# List available platforms and devices
platforms = cl.get_platforms()
for p in platforms:
    print(f"Platform: {p.name}")
    for d in p.get_devices():
        print(f"  Device: {d.name} (Type: {cl.device_type.to_string(d.type)})")

# Create context and queue (first platform/device)
ctx = cl.Context(devices=[platforms[0].get_devices()[0]])
queue = cl.CommandQueue(ctx)

# Prepare data
n = 10**6
a = np.random.rand(n).astype(np.float32)
b = np.random.rand(n).astype(np.float32)
c = np.empty_like(a)

# Create buffers
mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
c_buf = cl.Buffer(ctx, mf.WRITE_ONLY, a.nbytes)

# Kernel
program = cl.Program(ctx, """
__kernel void sum_vec(__global const float *a,
                      __global const float *b,
                      __global float *c)
{
    int gid = get_global_id(0);
    c[gid] = a[gid] + b[gid];
}
""").build()

# Execute
program.sum_vec(queue, a.shape, None, a_buf, b_buf, c_buf)
cl.enqueue_copy(queue, c, c_buf)

print("Correct result:", np.allclose(c, a + b))
