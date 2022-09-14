# DFS 문제 - 음료수 얼려 먹기
from collections import deque

# 입력 받기
# n, m: 얼음틀의 세로(행), 가로(열) 길이
# data: 얼음틀 정보
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# dfs로 특정 노드 방문 뒤, 인접 노드들 모두 방문 처리
def dfs(r, c):
    # 주어진 범위 벗어나면 즉시 종료
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    
    # 현재 노드가 방문 전이라면
    if graph[r][c] == 0:
        
        # 현재 노드 방문 처리
        graph[r][c] = 1

        # 인접 노드들 모두 방문 (상하좌우)
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        
        # 아이스크림 하나 완성
        return True

    # 현재 노드가 이미 방문 완료라면
    return False

# 모든 노드에 대해 음료수 채움
ice = 0     # 아이스크림 개수 초기화
for i in range(n):
    for k in range(m):
        # 모든 노드에 대해 dfs 수행
        if dfs(i, k) == True:
            ice += 1

# 결과 출력
print(ice)