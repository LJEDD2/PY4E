import random

computer_turn_num = random.randint(1, 3)

now = 1
while True:
    while True:
        my = input("My turn - 숫자를 입력하세요: ").split()
        flag = 1
        for i in range(len(my)):
            if not ('1' <= my[i] <= '9'):
                flag = 0
                break
            if int(my[i]) != now + i:
                flag = 0
                break
        if my == "" or not flag or int(my[0]) != now or not (1 <= len(my) <= 3):
            print("다시 입력해주세요.")
        else:
            print("플레이어 : ", end="")
            for i in my:
                print(i, end=" ")
            print()
            now = int(my[-1]) + 1
            if '31' in my:
                print("컴퓨터 win")
                exit(0)
            break
    computer_turn_num = random.randint(1, 3)
    computer = []
    for i in range(now, now + computer_turn_num):
        computer.append(i)
    print("컴퓨터 : ", end="")
    for i in computer:
        print(i, end=" ")
    print()
    if 31 in computer:
        print("플레이어 win")
        exit(0)
    now += computer_turn_num