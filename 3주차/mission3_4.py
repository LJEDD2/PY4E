# Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
# 소수: 1과 자기 자신만을 약수로 가지는 수

def count_prime_number(n,m):
    # 에라토스테네스의 체
    prime = [False,False] + [True]*(m-1)
    for i in range(2,m+1):
        if prime[i]:
            for j in range(2*i,m+1,i):
                prime[j] = False
           # n~m+1 범위의 소수의 개수 count하고 출력
    return prime[n:m+1].count(True)

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
print(f'소수개수 {count_prime_number(n, m)}')
