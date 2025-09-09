import pyopencl as cl 
import numpy as np 
import time
import math

cities = 1024
map_size = int(cities * (cities - 1) / 2)

if __name__ == "__main__":

    print('load program from cl file')
    f = open('city_distance.cl', 'r')
    kernels = ''.join(f.readlines())
    f.close()

    print('prepare data')
    start_time = time.time()
    city_x = np.random.random(cities).astype(np.float32)*100
    city_y = np.random.random(cities).astype(np.float32)*100
    final = np.zeros(map_size).astype(np.float32)
    time_hostdata_loaded = time.time()

    print('creat context')
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)
    print('create command queue')
    time_ctx_queue_creation = time.time()

    print('create memory on device')
    dev_x = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = city_x)
    dev_y = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf = city_y)
    dev_final = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final.nbytes)
    time_devicedata_loaded = time.time()

    print('compile kernel code')
    prg = cl.Program(ctx, kernels).build()
    time_kernel_compilation = time.time()

    print('excute kernel code')
    evt = prg.city_distance(queue, (map_size,), None, np.int32(cities), dev_x, dev_y, dev_final)
    evt.wait()
    time_kernel_execution = time.time()
    elapsed = 1e-9*(evt.profile.end - evt.profile.start)

    print('elapsed time: {}'.format(elapsed))
    time_before_readback = time.time()
    cl.enqueue_copy(queue, final, dev_final).wait()
    time_after_readback = time.time()

    print(final)
    print('Prepare host data took   : {}'.format(time_hostdata_loaded - start_time))
    print('Create CTX/QUEUE took    : {}'.format(time_ctx_queue_creation - time_hostdata_loaded))
    print('Upload data to device took  : {}'.format(time_devicedata_loaded - time_ctx_queue_creation))
    print('Complie kernel took      : {}'.format(time_kernel_compilation - time_devicedata_loaded))
    print('OpenCL elapsed time     : {}'.format(elapsed))
    print('Offload data from device took: {}'.format(time_after_readback - time_before_readback))
