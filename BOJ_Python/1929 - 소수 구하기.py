# BOJ 1929 - 소수 구하기

# 숫자 범위 입력 받기
start, end = map(int, input().split())

# 소수 함수 
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):     # 제곱근까지만 확인
        if n % i == 0:
            return False
    return True

# 소수 출력
if start == 1:
    start += 1

for num in range(start, end + 1):
    if isPrime(num):
        print(num)