# 기타 그래프 이론 실전 문제 - 크루스칼 알고리즘 - 팀 결성

# 특정 원소가 속한 집합 찾기
# find 함수 생성 (경로 압축 사용)
def find_parent(parent, x):

    # 부모 노드인지 확인해, 아니라면 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 함수 생성
def union_parent(parent, a, b):

    # 각자 부모노드 출력
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 부모노드가 둘의 부모노드로 갱신됨
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선의 개수 입력 받음
v, e = map(int, input().split())

# 부모 노드 리스트 초기화
parent = [0] * (v + 1)
for i in range(v + 1):
    parent[i] = i       # 부모 노드를 자기 자신으로 초기화


# 각 연산 하나씩 확인
for _ in range(e):
    oper, s, e = map(int, input().split())

    # 합치기 연산인 경우
    if oper == 0:
        union_parent(parent, s, e)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, s) == find_parent(parent, e):
            print('YES')
        else:
            print('NO')