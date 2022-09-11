### 그리디 예제 - 숫자 카드 게임 ###

N, M = map(int, input().split())
d = [[0] * M for _ in range(N)]
for i in range(N):
    d[i] = list(map(int, input().split()))

minD = list(min(d[i]) for i in range(N))
print(max(minD))