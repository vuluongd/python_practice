import pyopencl as cl
import numpy as np

# tạo context và queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
# chuẩn bị dữ liệu (mảng 12 phần tử)
N = 12
a_np = np.arange(N, dtype=np.int32)
global_size = (N,)
local_size = (4,)

#tạo buffer
mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
gid_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
lid_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
grp_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)

#kernel opencl
KERNELS ="""
__kernel void demo (__global const int *a, __global int *gid_out, __global int *lid_out, __global int *grp_out) {
    int gid = get_global_id(0);
    int lid = get_local_id(0);
    int grp = get_group_id(0);

    gid_out[gid] = gid;
    lid_out[gid] = lid;
    grp_out[gid] = grp;
}
"""
program = cl.Program(ctx, KERNELS).build()


#chạy kernel
program.demo(queue, global_size, local_size, a_g, gid_g, lid_g, grp_g)

#copy vào host
gid_np = np.empty_like(a_np)
lid_np = np.empty_like(a_np)
grp_np = np.empty_like(a_np)

cl.enqueue_copy(queue, gid_np, gid_g)
cl.enqueue_copy(queue, lid_np, lid_g)
cl.enqueue_copy(queue, grp_np, grp_g)

#in kết quả
print("Index | GlobalID | LocalID | GroupID")
for i in range(N):
    print(f"{i:5d} | {gid_np[i]:8d} | {lid_np[i]:7d} | {grp_np[i]:7d}")
