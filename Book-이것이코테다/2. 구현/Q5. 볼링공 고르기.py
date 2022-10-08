# 구현 알고리즘 기출문제 Q5. 볼링공 고르기

# 볼링공의 개수 n, 최대 무게 w 입력 받기
n, w = map(int, input().split())
# 각 볼링공의 무게 입력 받기
warr = list(map(int, input().split()))

# 결과 저장 변수
res = 0

# 하나씩 확인
for i in range(n):
    for j in range(i, n):
        if warr[i] != warr[j]:
            res += 1

# 결과 출력
print(res)