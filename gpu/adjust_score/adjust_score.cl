#ifndef __OPENCL_VERSION__
#define __kernel
#define __global
#endif
__kernel void adjust_score(__global int* values, __global int* final){
    int global_id = get_global_id(0);
    final[global_id] = convert_int(sqrt(convert_float(values[global_id]))*10);
}