# BOJ 2581 - 소수

# 범위 입력 받기 (start <= P <= end)
start = int(input())
end = int(input())

# 소수 담을 리스트
plist = []

# 소수 함수 생성
def isPrime(num):

    if num == 1:
        return -1
    else:
        # 2이상, 본인의 절반 이하의 범위의 수로 나누어 떨어지면 소수 X
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return -1
    # 어떤 수로도 나누어 떨어지지 않는다면 소수 O
    return 1

# 소수 찾기
for num in range(start, end + 1):
    if isPrime(num) > 0:
        plist.append(num)

# 결과 출력
if plist:    # 범위 내에 소수가 있으면, 소수 합과 최소 소수 값 출력
    print(sum(plist))
    print(min(plist))
else:           # 범위 내에 소수가 없으면, -1 출력
    print(-1)