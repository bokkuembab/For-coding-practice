# 최단 경로 실전 문제 - 전보

# 초기 설정
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시와 통로 개수 n과 m, 메시지 전송 도시 c 입력 받기
n, m, start = map(int, input().split())

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 통로 정보 저장을 위한 그래프 초기화
city = [[] for _ in range(n + 1)]
# 통로에 대한 경로 정보 입력 받기
for _ in range(m):
    s, d, c = map(int, input().split())
    city[s].append((d, c))

# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []      # 우선순위 큐

    # 시작 노드의 최단 거리는 0으로 설정, 큐에 저장
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:        
        # 큐가 비어있지 않은 동안에 가장 짧은 최단 거리 갖는 노드 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드이면 무시
        if distance[now] < dist:        
            continue

        # 현재 노드와 인접한 노드들 꺼내기
        for node in city[now]:
            cost = dist + node[1]
            
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드 중, 가장 멀리 있는 노드와의 최단 거리
count = 0   # 도달가능한 도시 수
max_distance = 0    # 가장 멀리 있는 노드와의 최단 거리
for d in distance:

    # 도달가능한 도시인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드도 count에 포함됨 (INF 값이 아니므로)
# 따라서, 시작노드를 제외해야 하므로 (count - 1) 해줌
count -= 1
print(count, max_distance)
