# Q3.2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.
# 단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)
# 중앙값: 정중앙에 있는 값
# 특정 두 숫자 사이의 수들을 리스트로 만드는 법
def find_even_number(n,m):
    if n%2 != 0:
        n += 1
    mid = int((n+m)/2)
    num = [i for i in range(n,m+1,2)]
    # 중앙값의 경우 str로 변환해서 한번 더 출력하기
    if mid in num:
        num.insert(num.index(mid)+1,str(mid))

    for i in num:
        if i != str(mid):
            print(f"{i} 짝수")
        else:
            print(f"{i} 중앙값")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)