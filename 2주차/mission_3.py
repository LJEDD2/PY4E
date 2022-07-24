"""
Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.

이름과 점수, 학점 모두 출력하도록 해봅니다.
"""
def grader(name,score):
    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f'학생이름:{name}\n점수:{score}\n학점:{grade}')

# main
import random

for score in [random.randint(40,100) for _ in range(5)]:
    grader("이호창",score)
    print()
