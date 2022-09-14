# BFS 문제 - 미로 탈출
# n(행), m(열): 미로의 크기
# 괴물이 있는/없는 부분: 0/1
# 출구는 n,m 위치
# 움직여야 하는 최소 칸의 개수

from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs 함수 정의
def bfs(r, c):

    # 큐 구현
    queue = deque()

    # 현재 위치 큐에 넣기
    queue.append((r, c))
    
    # 큐가 빌 때까지 확인
    while queue:

        # 큐 선입선출
        r, c = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            # 미로의 범위 넘어가면 무시
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
        
            # 괴물 있는 곳이면 무시
            if graph[nr][nc] == 0:
                continue

            # 안 가본 곳이면, 거리 1 늘리고, 큐에 넣기
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))

    # 최종 위치 도달 시 출력
    return graph[n - 1][m - 1]

# 결과 출력
print(bfs(0, 0))