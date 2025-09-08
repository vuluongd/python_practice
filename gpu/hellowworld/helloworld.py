import numpy
import pyopencl as cl
import time

TASKS = 64

if __name__ ==  '__main__':

    print ('load program from cl source file')
    f = open('helloworld.cl', 'r', encoding = 'utf-8')
    kernels = ''.join(f.readlines())
    f.close()

    print('prepare data')
    start_time = time.time()
    matrix = numpy.random.randint(low=1, high=101, dtype=numpy.int32, size=TASKS)
    time_hostdata_loaded = time.time()


    print('create context')
    ctx = cl.create_some_context()
    print('create command queue')
    queue = cl.CommandQueue(ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
    time_ctx_queue_created = time.time()

    print('prepare device memory for input / output')
    dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = matrix)
    time_devicedata_loaded = time.time()

    print('complie kernel code')
    prg = cl.Program(ctx, kernels).build()
    time_kernel_compilation = time.time()

    print('execute kernel program')
    evt = prg.hello_world(queue, (TASKS, ), (1, ), dev_matrix)
    evt.wait()
    elapse = 1e-9 * (evt.profile.end - evt.profile.start)
    print('done')

    print('Prepare host data took %.3f ms' % ((time_hostdata_loaded - start_time) * 1e3))
    print('Create context and queue took %.3f ms' % ((time_ctx_queue_created - time_hostdata_loaded) * 1e3))
    print('Load data to device took %.3f ms' % ((time_devicedata_loaded - time_ctx_queue_created) * 1e3))
    print('Kernel compilation took %.3f ms' % ((time_kernel_compilation - time_devicedata_loaded) * 1e3))
    print('Kernel execution took %.3f ms' % (elapse * 1e3))
    print('Total time took %.3f ms' % ((time_kernel_compilation - start_time) * 1e3))
    
