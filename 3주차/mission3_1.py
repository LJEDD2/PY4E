# 숫자를 입력받고 그 숫자의 구구단 출력
# 조건 1 홀수번째만 출력
# 조건 2 값이 50이하인 것만 출력

def gugudan(n):
    print(f"{n} 단")

    # 짝수번째 계산값만 출력
    for i in range(1,10,2):
        if n*i <= 50:
            print(f"{n} X {i} = {n*i}")

number = int(input("몇 단? :"))
gugudan(number)