#!/bin/bash
set -e

ENV_NAME="rocm-env"
ENV_PREFIX="$HOME/miniconda3/envs/$ENV_NAME"

echo ">>> [0/7] Kích hoạt conda và env $ENV_NAME"
if [ ! -d "$ENV_PREFIX" ]; then
  echo "❌ Không tìm thấy env $ENV_NAME tại $ENV_PREFIX"
  exit 1
fi
source ~/miniconda3/etc/profile.d/conda.sh
conda activate $ENV_NAME

# ---------------------------------------------------
echo ">>> [1/7] Gỡ PyTorch cũ (nếu có)"
pip uninstall -y torch torchvision torchaudio || true
conda remove -y torch torchvision torchaudio || true

# ---------------------------------------------------
echo ">>> [2/7] Cài dependency cần thiết"
pip install --upgrade pip
pip install pyyaml numpy typing_extensions cmake ninja wheel

# ---------------------------------------------------
echo ">>> [3/7] Clone repo rocm-build/navi14"
cd ~
if [ ! -d rocm-build ]; then
  git clone --recursive https://github.com/xuhuisheng/rocm-build.git
fi
cd rocm-build
git fetch
git checkout navi14
git pull
git submodule update --init --recursive

# ---------------------------------------------------
echo ">>> [4/7] Sửa env.sh để trỏ ROCM_PATH vào conda env"
sed -i "s|^ROCM_PATH=.*|ROCM_PATH=$ENV_PREFIX|" env.sh
grep "ROCM_PATH" env.sh

# ---------------------------------------------------
echo ">>> [5/7] Build ROCm Navi14"
# build lần lượt tất cả script, trừ khi muốn chỉ chọn vài package
for script in *.sh; do
    echo ">>> Đang build: $script"
    bash $script || { echo "❌ Lỗi khi build $script"; exit 1; }
done

# ---------------------------------------------------
echo ">>> [6/7] Build PyTorch ROCm (nếu repo hỗ trợ)"
if [ -f build_pytorch.sh ]; then
    ./build_pytorch.sh
else
    echo "⚠️ Không có build_pytorch.sh trong branch navi14, bạn cần build thủ công."
fi

# ---------------------------------------------------
echo ">>> [7/7] Kiểm tra cài đặt PyTorch ROCm"
python - <<'PYCODE'
import torch
print("Torch version:", torch.__version__)
print("HIP version:", getattr(torch.version, "hip", None))
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Device:", torch.cuda.get_device_name(0))
PYCODE

echo ">>> ✅ Hoàn tất build ROCm Navi14!"
