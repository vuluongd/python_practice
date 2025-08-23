import torch

device = torch.device("cuda")

# Tạo tensor lớn và nhân ma trận
a = torch.randn(1000, 1000, device=device)
b = torch.randn(1000, 1000, device=device)
c = torch.matmul(a, b)

print("Kết quả shape:", c.shape)
print("Thiết bị đang chạy:", c.device)