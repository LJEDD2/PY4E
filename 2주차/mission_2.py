"""
Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
"""
def yearly_payment(payment):
    if 0 <= payment <= 1200:
        tax_rate = 0.06
    elif 1200 < payment <= 4600:
        tax_rate = 0.15
    elif 4600 < payment <= 8800:
        tax_rate = 0.24
    elif 8800 < payment <= 15000:
        tax_rate = 0.35
    elif 15000 < payment <= 30000:
        tax_rate = 0.38
    elif 30000 < payment <= 50000:
        tax_rate = 0.4
    else:
        tax_rate = 0.42

    # 억, 만 구분
    def split_money(money):
        money = str(money)
        if len(money) > 4:
            return money[:-4] + '억' + str(int(money[-4:])) + "만"
        else:
            return money + "만"

    print(f"세전 연봉:{split_money(payment)}원\n세후 연봉:{split_money(int(payment - payment * tax_rate))}원")


# 입력
monthly_payment = int(input("월급을 입력하세요 : "))
# 출력
yearly_payment(12*monthly_payment)