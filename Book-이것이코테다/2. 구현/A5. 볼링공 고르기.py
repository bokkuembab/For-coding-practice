# 구현 알고리즘 기출문제 Q5. 볼링공 고르기
# 도서 풀이

# 볼링공의 개수 n, 최대 무게 w 입력 받기
n, w = map(int, input().split())
# 각 볼링공의 무게 입력 받기
warr = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in warr:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

res = 0
# 1부터 m까지의 각 무게에 대해 처리
for i in range(1, w + 1):
    n -= array[i]   # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    res += array[i] * n     # B가 선택하는 경우의 수와 곱하기

# 결과 출력
print(res)