import math
import pyopencl as cl
import numpy as np
import time

tasks = 1048576
cl_tasks = int(tasks/4)

if __name__ == "__main__":
    print('load program from cl source file')
    f = open('adjust_score_2.cl', 'r', encoding = 'utf-8')
    kernels = ''.join(f.readlines())
    f.close()

    print('prepare data ...')
    start_time = time.time()
    matrix = np.random.randint(low=1, high =101, dtype=np.int32, size = tasks)

    #prepare memory for final answer from opencl
    final = np.zeros(tasks, dtype=np.int32)
    time_hostdata_loaded = time.time()

    print('creat context')
    ctx = cl.create_some_context()
    print('creat command queue')
    queue = cl.CommandQueue(ctx, properties = cl.command_queue_properties.PROFILING_ENABLE)
    time_ctx_queue_creation = time.time()

    print('create on memory on device')
    dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = matrix)
    dev_final = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final.nbytes)
    time_devicedata_loaded = time.time()

    print('compile kernel code')
    prg = cl.Program(ctx, kernels).build()
    time_kernel_compilation = time.time()

    print('execute kernel programs')
    evt = prg.adjust_score(queue,(cl_tasks,), (1, ), dev_matrix, dev_final)
    print('wait for kernel executions')
    evt.wait()
    elapsed = 1e-9 * (evt.profile.end - evt.profile.start)

    time_before_readback = time.time()
    cl.enqueue_copy(queue, final, dev_final).wait()
    time_after_readback = time.time()

    #prepare data for comparison
    correct = np.zeros(tasks, dtype=np.int32)
    python_start_time = time.time()
    for i in range(0, tasks):
        correct[i] = math.floor(math.sqrt(matrix[i]) * 10)
    python_end_time = time.time()

    equal = np.all(correct == final)

    print(final)
    print('Prepare hosta data took      : {}'.format(time_hostdata_loaded - start_time))
    print('Create CTX/QUEUE took        : {}'.format(time_ctx_queue_creation -time_hostdata_loaded))
    print('Upload data to device tool   : {}'.format(time_devicedata_loaded - time_ctx_queue_creation))
    print('Compile kernel took          : {}'.format(time_kernel_compilation - time_devicedata_loaded))
    print('OpenCL elapsed time          : {}'.format(elapsed))
    print('Offload data from device took: {}'.format(time_after_readback - time_before_readback))
    print('Python execution took        : {}'.format(python_end_time - python_start_time))

    if not equal:
        print('Results doesnot match!!')
    else:
        print('Results is OK')


    



