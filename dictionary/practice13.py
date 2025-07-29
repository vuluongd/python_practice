score = {
    "alice" : 10,
    "luong" :15,
    "dung": 20,
}
max_score = max(score.values())
print(f"điểm cao nhất: {max_score}")
top_student = max(score, key = score.get)
print(f"Người được điểm cao nhất: {top_student}")
