__kernel void adjust_score(__global int4* values, __global int4* final) {
    int global_id = get_global_id(0);

    float4 float_value = (float4) (values[global_id].x, values[global_id].y, values[gloabal_id].z, values[global_id].z, values[globa_id].w);
    float4 float_final = sqrt(float_value) * 10;

    final[global_id] = (int) (float_final.x, float_final.y, float_final.z, float_final.w);
    
}