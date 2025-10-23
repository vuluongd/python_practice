names = ['bob', 'luong', 'dylan', 'dung', 'cylan']
for i, name in enumerate(names):
    if i == 0:
        continue
    prev_name = names[i - 1]
    print(f"Trước {name} là {prev_name}")