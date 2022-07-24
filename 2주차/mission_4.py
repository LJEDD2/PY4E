"""
Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.
"""
def bus_fare(age,type):
    payment_type = {"카드":0,"현금":1}
    payment = "450원"
    if payment_type[type]:
        if age < 8 or age >= 75 :
            payment = "무료"
        elif age >= 20:
            payment = "1300원"
        elif age >= 14 :
            payment = "1000원"
    else:
        if age < 8 or age >= 75:
            payment = "무료"
        elif age >= 20:
            payment = "1200원"
        elif age >= 14:
            payment = "720원"

    print(f'나이:{age}세\n지불유형:{type}\n버스요금:{payment}')

# main
bus_fare(30, "현금")
bus_fare(10, "현금")
bus_fare(3, "카드")
bus_fare(40, "현금")
bus_fare(80, "카드")
bus_fare(15, "카드")
bus_fare(18, "현금")

