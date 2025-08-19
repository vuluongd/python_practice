#!/bin/bash
# Script dọn sạch PyTorch CUDA và cài PyTorch ROCm trong môi trường conda

# Nạp conda vào shell
source ~/miniconda3/etc/profile.d/conda.sh

echo ">>> [1] Kích hoạt base..."
conda activate base

echo ">>> [2] Gỡ PyTorch cũ (nếu có)..."
pip uninstall -y torch torchvision torchaudio
conda remove -y torch torchvision torchaudio || true

echo ">>> [3] Tạo môi trường mới rocm-env..."
conda create -n rocm-env python=3.10 -y

echo ">>> [4] Kích hoạt môi trường rocm-env..."
conda activate rocm-env

echo ">>> [5] Cài PyTorch ROCm..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0

echo ">>> ✅ Hoàn tất!"
echo "Bây giờ gõ: conda activate rocm-env"
echo "Sau đó kiểm tra bằng Python:"
echo "  import torch"
echo "  print(torch.version.hip)"
echo "  print(torch.cuda.is_available())"
echo "  print(torch.cuda.get_device_name(0))"

