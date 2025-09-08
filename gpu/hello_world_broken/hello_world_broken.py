import pyopencl as cl

TASKS = 64

if __name__ == '__main__':
    print('creat context')
    ctx = cl.create_some_context()

    print('create command queue')
    queue = cl.CommandQueue(ctx)

    print('load program from cl source file')
    f = open('hello_world_broken.cl', 'r', encoding='utf-8')
    kernels = ''.join(f.readlines())
    f.close()

    print('complie kernel code')
    prg = cl.Program(ctx, kernels).build()

    print('execute kernel program')
    evt = prg.hello_world(queue, (TASKS,), (1,))
    evt.wait()
    print('done')