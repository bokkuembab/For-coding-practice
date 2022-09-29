# 기타 그래프 이론 - 크루스칼 알고리즘 - 도시 분할 계획
# 두 마을로 나누기 위해서는 신장 트리 구현 후, 가장 비용 큰 간선 제거

# find 함수 생성 (압축 경로 이용)
def find_parent(parent, x):

    # 부모 노드가 아니라면, 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    # 부모 노드 출력
    return parent[x]

# union 함수 생성
def union_parent(parent, a, b):

    # 각 부모 노드 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 부모 노드로 합치기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선의 개수 입력 받기
v, e = map(int, input().split())

# 간선 정보 리스트 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i   # 부모 노드를 자기 자신으로 초기화

    
# 간선 정보 입력받기
edges = []
for _ in range(e):
    s, e, c = map(int, input().split())
    edges.append((c, s, e))     # 비용 순으로 정렬하기 위해 비용 먼저 저장

# 간선을 비용 순으로 정렬
edges.sort()

# 최종 비용 저장 변수
result = 0
# 최소 신장 트리에 포함되는 간선 중, 가장 비용이 큰 간선
last = 0

# 간선을 하나씩 확인하며, 사이클 발생하지 않으면 집합에 포함
for edge in edges:
    c, s, e = edge

    # 사이클 발생 여부 확인
    # 부모 노드가 같으면 사이클 발생
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result += c
        last = c

# 결과 출력
print(result - last)