def make_comma(n):
    n = str(n)[::-1] # 0이 3개 들어올 때 마다 ,을 넣기 위해 거꾸로 뒤집어 줌
    new = ""
    cnt = 0
    for i in n: # 문자열을 뒤집어 새로운 문자열에 하나씩 숫자를 넣을 것임
        cnt += 1
        new += i
        if cnt%3==0 : # 숫자를 넣은 횟수가 3의 배수일때
            new += ',' # ,로 구분
    print(new[::-1] if new[-1] !=',' else new[::-1][1:]) # 다시 뒤집어서 출력, 맨 앞에 ','가 있을 경우 제거하고 출력

test = "1"
for i in range(10):
    make_comma(int(test))
    test += "0"