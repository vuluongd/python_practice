import torch
print("Torch version:", torch.__version__)
print("Build HIP version:", torch.version.hip)
print("Build CUDA version:", torch.version.cuda)
print("Available devices:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print(f" - Device {i}: {torch.cuda.get_device_name(i)}")