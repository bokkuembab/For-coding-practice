# 구현 알고리즘 기출문제 Q4. 만들 수 없는 금액
# 나의 풀이

# 동전 개수, 각 동전들의 가치 입력 받기
numc = int(input())
coins = list(map(int, input().split()))

# 동전들 큰 순서대로 정렬
coins.sort(reverse=True)

# 만들 수 없는 금액
res = 0

# 1원부터 만들 수 있는지 확인
for mon in range(1, 1000000):
    res = mon
    for c in coins:
        if mon - c >= 0:
            mon -= c
    if mon > 0:
        break
  
# 결과값 출력
print(res)