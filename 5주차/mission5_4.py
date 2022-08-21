from datetime import datetime
from dateutil.relativedelta import relativedelta

arr = ["월", "화", "수", "목", "금", "토", "일"]
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def after_100(n, m, k):
    my_date = datetime(2019, n, m)
    new_date = my_date + relativedelta(days=99)
    ans = str(new_date.date())
    a, b, c = ans.split('-')
    print(f"{n}월 {m}일 {k}요일부터 100일 뒤는 {b}월 {c}일 {arr[(arr.index(k) + 1) % 7]}요일")


while True:
    try:
        n = int(input("몇 월? (숫자로 입력) : "))
    except ValueError:
        print("다시 입력해주세요.")
        continue
    if 1 <= n <= 12:
        break
    else:
        print("다시 입력해주세요.")
        continue

while True:
    try:
        m = int(input("몇 일? (숫자로 입력) : "))
    except ValueError:
        print("다시 입력해주세요.")
        continue
    if 1 <= m <= day[n]:
        break
    else:
        print("다시 입력해주세요.")
        continue
while True:
    k = input("무슨 요일? (한글로 한 글자만 입력) : ")
    if k not in arr:
        print("다시 입력해주세요.")
    else:
        break
after_100(n, m, k)