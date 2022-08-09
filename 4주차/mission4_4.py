def check_id(p):
    if p.find('-') != 6 or len(p) != 14 :
        print('잘못된 번호입니다.\n올바른 번호를 넣어주세요')
        return
    sex = "여자" if p[7] in ['2','4'] else "남자"
    if "00" <= p[:2] <= "22":
        ques = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if ques == "o":
            if p[7] not in ["3","4"]:
                print('잘못된 번호입니다.\n올바른 번호를 넣어주세요')
                return
        elif ques == "x":
            if p[7] in ["3","4"]:
                print('잘못된 번호입니다.\n올바른 번호를 넣어주세요')
                return
        else:
            print('잘못된 번호입니다.\n올바른 번호를 넣어주세요')
            return

    print(f"{p[:2]}년{p[2:4]}월", sex)

a = input("주민번호를 입력하세요: ")
check_id(a)