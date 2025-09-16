import math
import numpy as np
import pyopencl as cl
import time 

tasks = 1000000
cl_tasks = tasks // 4

#kernel code
KERNELS = """
__kernel void adjust_score_scalar(__global int* values, __global int* final){
    int gid = get_global_id(0);
    final[gid] = (int)floor(sqrt((float)values[gid]) * 10.0f);
    }

__kernel void adjust_score_vector(__global int4* values, __global int4* final){
    int gid = get_global_id(0);
    float4 v = convert_float4(values[gid]);
    float4 r = sqrt(v) * 10.0f;
    final[gid] = convert_int4(r);
}
"""
if __name__ == "__main__":

    matrix = np.random.randint(1, 101, size=tasks).astype(np.int32)
    final_scalar = np.zeros(tasks, dtype=np.int32)
    final_vector = np.zeros(tasks, dtype=np.int32)

    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)

    prg = cl.Program(ctx, KERNELS).build()
    #=================scalar==========================
    dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = matrix)
    dev_final_scalar = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final_scalar.nbytes)

    evt = prg.adjust_score_scalar(queue, (tasks,), None, dev_matrix, dev_final_scalar)
    evt.wait()
    time_scalar = 1e-9 * (evt.profile.end - evt.profile.start)

    cl.enqueue_copy(queue, final_scalar, dev_final_scalar).wait()


    #=================vector=========================
    matrix4 = matrix.reshape(cl_tasks,4).view(np.int32)
    final4 = np.zeros((cl_tasks, 4), dtype=np.int32)

    dev_matrix4 = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = matrix4)
    dev_final4 = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final4.nbytes)

    evt = prg.adjust_score_vector(queue, (cl_tasks,), None, dev_matrix4, dev_final4)
    evt.wait()
    time_vector = 1e-9 * (evt.profile.end - evt.profile.start)

    cl.enqueue_copy(queue, final4, dev_final4).wait()
    final_vector = final4.reshape(tasks)

     # ================== Kiểm chứng ==================
    correct = np.floor(np.sqrt(matrix) *10).astype(np.int32)
    print("scalar corrcect:", np.all(correct == final_scalar))
    print("vector correct:", np.all(correct == final_vector))
    print("Thời gian Scalar kernel: {:.6f} s".format(time_scalar))
    print("Thời gian Vector kernel: {:.6f} s".format(time_vector))

    




