# 다이나믹 프로그래밍 실전 문제 - 개미 전사

# 식량창고의 개수 입력 받기
n = int(input())

# 각 식량창고에 저장된 식량의 개수 입력 받기
k = list(map(int, input().split()))

# 미리 계산한 결과 저장을 위한 DP 테이블 초기화
dp = [0] * 100

# 다이나믹 프로그래밍 진행 - bottom-up 방식
dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + k[i])

# 결과값 출력
print(dp[n - 1])