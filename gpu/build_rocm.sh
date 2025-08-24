#!/bin/bash
set -e

PYTORCH_SRC=$HOME/pytorch
cd $PYTORCH_SRC

echo ">>> Vá toàn bộ CMakeLists.txt về cmake >= 3.5..."

find third_party -name "CMakeLists.txt" | while read -r f; do
    echo "  -> Vá $f"
    # Bỏ qua comment, thay mọi phiên bản nhỏ hơn 3.5 thành 3.5...3.25
    sed -i -E 's/cmake_minimum_required\s*\(VERSION [0-9]+\.[0-9]+.*\)/cmake_minimum_required(VERSION 3.5...3.25)/I' "$f"
done

echo ">>> Dọn build cũ..."
python3 setup.py clean || true
rm -rf build

echo ">>> Build lại PyTorch ROCm..."
CMAKE_COMMAND=$HOME/miniconda3/envs/rocm-env/bin/cmake \
USE_CUDA=0 USE_XPU=0 USE_ROCM=1 \
python3 setup.py bdist_wheel

