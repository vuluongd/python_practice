def convert_score_to_grade(score):
    grade_dict = {
        (0, 59) : "F",
        (60,69) : "D",
        (70,79) : "C",
        (80,89) : "B",
        (90,100): "A"

    }
    for (a,b),grade in grade_dict.items():
        if a <= score <=b:
            return grade

score = int(input("score: "))

print(f"Your grade: {convert_score_to_grade(score)}")
