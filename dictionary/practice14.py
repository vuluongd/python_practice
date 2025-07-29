import random

students = ["an", "hùng","nam", "huy"]
scores = {student: random.randint(0,100) for student in students}

print("Đoán xem ai cao điểm nhất")

print("Danh sách học sinh")
for name in scores.keys():
    print (name)

guess = input("Ai là người cao điểm ")
guess_score = scores[guess]

top_student = max(scores, key=scores.get)
top_score = scores[top_student]

if guess == top_student:
    print (f"đúng rồi {top_student} là người đạt điểm cao nhất với {top_score} điểm")
else:
    print (f"sai {top_student} mới là nguời đạt điểm cao nất với {top_score} điểm, {guess} chỉ đạt {guess_score} điểm")

print ("kết quả cuối cùng")
for name, score in scores.items():
    print(f"{name}: {score}")
