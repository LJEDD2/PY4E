try:
    for i in [3,2,1]:
        print(1 / i)
except ZeroDivisionError:
    print("0으로 나눌 수 없음 ")
else:
    print("실행완료")
finally:
    print("good")