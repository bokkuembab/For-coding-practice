# BOJ 1978 - 소수 찾기

# 주어지는 숫자 개수, 숫자들 입력 받기
n = int(input())
nlist = list(map(int, input().split()))

# 소수 함수 생성
def isPrime(n):
    if n == 1:
        return -1
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return -1
    return 1

# 주어진 수 중 소수 몇 개인지 찾기
pnum = 0
for n in nlist:
    if isPrime(n) > 0:
        pnum += 1

# 결과 출력
print(pnum)