import torch

print("HIP version:", torch.version.hip)
print("CUDA available:", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0))