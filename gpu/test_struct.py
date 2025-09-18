import numpy as np
import pyopencl as cl
import pyopencl.tools 
import pyopencl.array


ctx = cl.create_some_context(interactive=False)

queue = cl.CommandQueue(ctx)

my_struct = np.dtype([("field1", np.int32), ("field2", np.float32)])
print(my_struct)
# [('field1', '<i4'), ('field2', '<f4')]
#Chuyển dtype của NumPy về struct trong C (OpenCL).”
my_struct, my_struct_c_decl = cl.tools.match_dtype_to_c_struct(
    ctx.devices[0], "my_struct", my_struct
)
print(my_struct_c_decl)
'''
typedef struct {
  int field1;
  float field2;
} my_struct;

'''
my_struct = cl.tools.get_or_register_dtype("my_struct", my_struct)
ary_host = np.empty(20, my_struct)
ary_host["field1"].fill(217)
ary_host["field2"].fill(1000)
ary_host[13]["field2"] = 12
print(ary_host)
'''
[(217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.)
 (217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.)
 (217, 1000.) (217, 1000.) (217, 1000.) (217,   12.) (217, 1000.)
 (217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.) (217, 1000.)]
'''

ary = cl.array.to_device(queue, ary_host)

KERNELS = """
__kernel void set_to_1(__global my_struct *a) {
    a[get_global_id(0)].field1 = 1;
}
"""
prg = cl.Program(ctx, my_struct_c_decl + KERNELS).build()
evt = prg.set_to_1(queue, ary.shape, None, ary.data)

print(ary)

'''
[(1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.)
 (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.)
 (1, 1000.) (1,   12.) (1, 1000.) (1, 1000.) (1, 1000.) (1, 1000.)
 (1, 1000.) (1, 1000.)]
'''
from pyopencl.elementwise import ElementwiseKernel

elwise = ElementwiseKernel(ctx, "my_struct *a", "a[i].field1 = 2", preamble=my_struct_c_decl)

evt = elwise(ary)
print(ary)
'''
[(2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.)
 (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.)
 (2, 1000.) (2,   12.) (2, 1000.) (2, 1000.) (2, 1000.) (2, 1000.)
 (2, 1000.) (2, 1000.)]

'''
