# 구현 알고리즘 기출문제 Q4. 만들 수 없는 금액
# 도서 풀이

# 동전 개수, 각 동전들의 가치 입력 받기
numc = int(input())
coins = list(map(int, input().split()))

# 동전들 오름차순 정렬
coins.sort()

# 만들 수 있는 금액 저장 변수
target = 1

# 마지막 target 값은 (N개의 숫자를 모두 더한 값 + 1) 이므로
# 중간에 break되지 않는다면, (N개의 숫자로 만들 수 있는 최대 수 + 1)로 끝남
for x in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    # 작은 수부터 차례대로 더하게 됨
    target += x

# 만들 수 없는 금액 출력
print(target)