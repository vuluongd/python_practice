import math
import numpy 
import pyopencl as cl
import time

TASKS = 64
if __name__ ==  '__main__':
    print('load program from cl source file')
    f = open('adjust_score.cl', 'r', encoding = 'utf-8')
    kernels = ''.join(f.readlines())
    f.close()

    print('prepare data')
    start_time = time.time()
    matrix = numpy.random.randint(low=1, high=101, dtype=numpy.int32, size=TASKS)
    # prepare memory for final answer from opencl
    final = numpy.zeros(TASKS, dtype=numpy.int32)
    time_hostdata__loaded = time.time()

    print('create context')
    ctx = cl.create_some_context()
    print('create command queue')
    queue = cl.CommandQueue(ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
    time_ctx_queue_creation = time.time()

    print('prepare device memory for input / output')
    dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf= matrix)
    dev_final = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final.nbytes)
    time_devicedata_loaded = time.time()
    
    print('complie kernel code')
    prg = cl.Program(ctx, kernels).build()
    time_kernel_compilation = time.time()

    print('execute kernel program')
    evt = prg.adjust_score(queue, (TASKS, ), (1, ), dev_matrix, dev_final)
    print('wait for kernel executions')
    evt.wait()
    elapsed = 1e-9 * (evt.profile.end - evt.profile.start)

    time_before_readback = time.time()
    cl.enqueue_copy(queue, final, dev_final).wait()
    time_after_readback = time.time()

    # prepare data for comparison
    correct = numpy.zeros(TASKS, dtype = numpy.int32)
    python_start_time = time.time()

    #prepare data for comparision
    correct = numpy.zeros(TASKS, dtype=numpy.int32)
    python_start_time = time.time()
    for i in range(0, TASKS):
        correct[i] = int(math.sqrt(float(matrix[i]))*10)

    python_end_time = time.time()
    
    equal = numpy.all(correct == final)

    print(final)
    print('Prepare host data took'  '%.3f ms' % ((time_hostdata__loaded - start_time) * 1e3))
    print('Create context and queue took %.3f ms' % ((time_ctx_queue_creation - time_hostdata__loaded) * 1e3))
    print('Load data to device took %.3f ms' % ((time_devicedata_loaded - time_ctx_queue_creation) * 1e3))
    print('Kernel compilation took %.3f ms' % ((time_kernel_compilation - time_devicedata_loaded) * 1e3))
    print('Kernel execution took %.3f ms' % (elapsed * 1e3))
    print('Readback from device took %.3f ms' % ((time_after_readback - time_before_readback) * 1e3))
    print('Python calculation took %.3f ms' % ((python_end_time - python_start_time) * 1e3))
    print('Total time took %.3f ms' % ((time_after_readback - start_time) * 1e3))   

    if not equal:
        print('Results doesnot match')
    else:
        print('Results match')


