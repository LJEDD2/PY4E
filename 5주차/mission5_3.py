import random

dict1 = dict()
dict2 = dict()
arr = []
ans = []
while len(arr) != 3:
    num = random.randint(0, 100)
    if num in dict1.keys():
        continue
    dict1[num] = 1
    arr.append(num)
arr.sort()

turn = 1
while True:
    print(f"{turn}차 시도")
    n = int(input("숫자를 예측해보세요 : "))
    if not (1 <= n <= 100):
        print("1이상 100이하의 정수를 입력해주세요.")
        continue
    if n in dict2.keys():
        print("이미 예측에 사용된 숫자입니다.")
    else:
        dict2[n] = 1
        if n == arr[0]:
            print(f"숫자를 맞추셨습니다! {n}는 최솟값입니다.")
            ans.append(n)
        elif n == arr[1]:
            print(f"숫자를 맞추셨습니다! {n}는 중간값입니다.")
            ans.append(n)
        elif n == arr[2]:
            print(f"숫자를 맞추셨습니다! {n}는 최댓값입니다.")
            ans.append(n)
        else:
            print(f"{n}는 없습니다.")
        if len(ans) != 3 and turn:
            if arr[0] not in ans:
                if n < arr[0]:
                    print(f"최솟값은 {n}보다 큽니다.")
                else:
                    print(f"최솟값은 {n}보다 작습니다.")
            if arr[2] not in ans:
                if n < arr[2]:
                    print(f"최댓값은 {n}보다 큽니다.")
                else:
                    print(f"최댓값은 {n}보다 작습니다.")
    if len(ans) == 2:
        print(f"{turn}번 시도만에 예측 성공")
        break
    turn += 1