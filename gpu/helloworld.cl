
__kernel void hello_world(__global int* output){
    int global_id = get_global_id(0);
    printf("Hello, World from work-item #%d, got value: %d\n", global_id, output[global_id]);
}
