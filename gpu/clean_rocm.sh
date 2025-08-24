#!/bin/bash
set -e

echo ">>> [1/5] Deactivate conda env nếu đang chạy"
conda deactivate || true

echo ">>> [2/5] Xóa conda env rocm-env (nếu có)"
conda remove -n rocm-env --all -y || true

echo ">>> [3/5] Xóa thư mục ROCm mặc định trong /opt"
sudo rm -rf /opt/rocm /opt/rocm-*

echo ">>> [4/5] Xóa thư mục build cũ trong home"
rm -rf ~/rocm-build ~/ROCm-Device-Libs ~/rocBLAS ~/MIOpen ~/rocRAND ~/rocPRIM
rm -rf ~/ROCm ~/ROCmProject

echo ">>> [5/5] Xóa cache pip và cmake"
rm -rf ~/.cache/rocm* ~/.cache/pip ~/.cmake

echo ">>> Hoàn tất: ROCm đã được gỡ sạch. Giờ bạn có thể build lại từ đầu."
