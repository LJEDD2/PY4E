#Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
# 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
# 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
# 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
import random

def rsp_advanced(n):
    # 0 : 승리 / 1 : 무승부 / 2 : 패배
    score_my = {0: 0, 1: 0, 2: 0}
    score_com = {0: 0, 1: 0, 2: 0}
    for i in range(1,n+1):
        # MY, COM
        game = {("가위", "바위"): ["컴퓨터 승리!",2], ("보", "가위"): ["컴퓨터 승리!",2], ("바위", "보"): ["컴퓨터 승리!",2],
                ("바위", "가위"): ["나의 승리!", 0], ("가위", "보"): ["나의 승리!", 0], ("보", "바위"): ["나의 승리!", 0]}

        rsp = ["가위", "바위", "보"]

        # 입력 범위 벗어나면 다시 입력받기
        while True:
            MY = input("가위 바위 보 : ")
            if MY in ["0","1","2","가위", "바위", "보"]:
                break

        if MY in ["0","1","2"]:
            MY = rsp[int(MY)]
        COM = rsp[random.randint(0, 2)]
        print(f"나:{MY} \n컴퓨터:{COM}")

        if COM!=MY:
            print(f'{i} 번째 판 {game[(MY, COM)][0]}\n')
            # 성적 입력
            score_my[game[(MY, COM)][1]] += 1
            score_com[game[(COM, MY)][1]] += 1

        else:
            #무승부
            score_my[1] += 1
            score_com[1] +=1

    print('|---------결과---------|')
    print(f"나의 전적: {score_my[0]}승 {score_my[1]}무 {score_my[2]}패")
    print(f"컴퓨터의 전적: {score_com[0]}승 {score_com[1]}무 {score_com[2]}패")


try:
    games = int(input("몇 판을 진행하시겠습니까? :"))
    if games <= 0:
        raise Exception("0 이상의 숫자를 입력해 주세요") # 예외를 발생시킴
    rsp_advanced(games)

except Exception as e: # 예외가 발생한 경우 에러
    print(e)

