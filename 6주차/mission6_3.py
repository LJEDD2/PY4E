# Q3. 예금 금리가 너무 낮아서 주식을 시작했습니다.
# 아래와 같이 매수한 종목 이름, 수량, 매수 평균 금액이 있습니다.
# 판매가는 따로 주어집니다. 종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요.(소수 둘째자리까지 출력)


# 수익률(%) = (판매가 - 매수평균금액) / 매수평균금액 * 100
def stock_profit(stock, sell):
    name, cnt, st = stock.split('/') # '/'로 기업명, 수량, 매수평균금액 분리
    cnt, st = int(cnt),int(st) # 숫자형으로 변환

    # 이름과 수익률을 반환
    return [name,(sell-st)/st*100]

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
result = []

for stock,sell in zip(stocks.split(','),sells): # 크게 ','로 구분되어있음
    result.append(stock_profit(stock,sell)) # 결과 리스트에 기업 하나씩 저장

for i in sorted(result,key=lambda x : -x[1]): # 수익률을 기준으로 오름차순 정렬
    print(f'{i[0]}의 수익률 {i[1]:.2f}') # 이름과 수익률 출력

