#!/bin/bash
set -e

echo ">>> [1/6] Kích hoạt môi trường build"
# Đảm bảo bạn đã conda activate rocm-env trước khi chạy
ENV_PREFIX="$HOME/miniconda3/envs/rocm-env"

if [ ! -d "$ENV_PREFIX" ]; then
  echo "❌ Không tìm thấy môi trường rocm-env ở $ENV_PREFIX"
  exit 1
fi

export PATH="$ENV_PREFIX/bin:$PATH"

echo ">>> [2/6] Cài dependency Python (pyyaml, numpy, typing-extensions, cmake, ninja)"
pip install --upgrade pip
pip install pyyaml numpy typing_extensions cmake ninja

echo ">>> [3/6] Clone PyTorch (nếu chưa có)"
cd ~
if [ ! -d pytorch ]; then
  git clone --recursive https://github.com/pytorch/pytorch.git
else
  echo "Repo pytorch đã tồn tại, update submodule..."
  cd pytorch
  git submodule sync
  git submodule update --init --recursive
  cd ..
fi

echo ">>> [4/6] Clean build cũ"
cd ~/pytorch
python3 setup.py clean || true
rm -rf build

echo ">>> [5/6] Build PyTorch ROCm wheel"
USE_CUDA=0 USE_XPU=0 USE_ROCM=1 python3 setup.py bdist_wheel

echo ">>> [6/6] Cài đặt wheel vừa build"
pip install dist/torch-*.whl --force-reinstall

echo ">>> ✅ Build & cài đặt PyTorch ROCm hoàn tất!"
python3 -c "import torch; print('Torch version:', torch.__version__); print('HIP version:', torch.version.hip); print('Available devices:', torch.cuda.device_count())"
