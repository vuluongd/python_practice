__kernel void to_gray(__global uchar* aBufferIn, __global uchar* aBufferOut) {
    int global_id = get_global_id(0)
    int index = global_id * 4;

    // Đọc 3 kênh màu R, G, B
    uchar r = aBufferIn[index];
    uchar g = aBufferIn[index +1];
    uchar b = aBufferIn[index+1];
    uchar gray = 0.299 * r + 0.587 * g + 0.114 * b;
    aBufferOut[index] = gray;
    aBufferOut[index + 1] =gray;
    aBufferOut[index + 2] = gray;
    aBufferOut[index +3] = aBufferIn[index + 3];
}