# 최단 경로 실전 문제 - 미래 도시

# 회사, 경로의 개수 입력 받기
n, m = map(int, input().split())
start = 1       # 나의 위치

# 최단 거리 저장할 그래프 초기화 (2차원 리스트)
INF = int(1e9)      # 최단거리 값을 초기화할 무한대 설정
company = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신으로 가는 거리 비용 0으로 설정
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            company[i][j] = 0

# 경로 정보 입력 받기
for _ in range(m):

    # 연결된 회사 입력 받아, 서로 이동하는 거리 1로 설정
    s, d = map(int, input().split())
    company[s][d] = 1
    company[d][s] = 1

# 최종 도착 노드, 거쳐갈 노드 입력 받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for s in range(1, n + 1):
        for d in range(1, n + 1):
            company[s][d] = min(company[s][d], company[s][k] + company[k][d])

# 수행 결과 출력
result = company[start][k] + company[k][x]

# 도달 불가능한 경우, -1 출력
if result >= INF:
    print(-1)
# 도달 가능하다면, 최단 거리 출력
else:
    print(result)