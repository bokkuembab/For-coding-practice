# 기타 그래프 이론 - 위상 정렬 알고리즘 - 커리큘럼

from collections import deque   # 큐 생성을 위한 라이브러리
import copy     # 리스트 복사를 위한 라이브러리

# 강의(노드) 개수 입력 받기
v = int(input())

# 변수들 초기화
indegree = [0] * (v + 1)      # 진입 차수 저장 리스트
graph = [[] for _ in range(v + 1)]       # 각 강의의 선수과목(연결된 간선 정보) 연결 리스트
time = [0] * (v + 1)    # 각 강의의 강의 시간 리스트

# 각 강의의 강의 시간, 선수 과목 입력 받기
for i in range(1, v + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]   # 강의 시간 저장
    for pre in info[1:-1]:      # 마지막은 -1 값 가지므로 제외
        indegree[i] += 1    # 진입 차수 1 증가
        graph[pre].append(i)    # 선수 과목에 현재 강의 넣음

# 위상 정렬 함수 생성
def topology_sort():
    result = copy.deepcopy(time)     # 각 강의를 듣기 위해 걸리는 총 시간 (선수과목+현재 강의)
    q = deque()     # 큐 생성

    # 처음 시작 시, 진입 차수가 0인 강의(노드)를 큐에 넣음
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:

        # 현재 큐에 저장된 값 꺼내기
        now = q.popleft()

        # 해당 원소의 다음 수강 과목 하나씩 확인 (연결 노드들 넣기)
        for lec in graph[now]:

            # 연결된 경로의 합을 더함 (선수 과목 시간 + 현재 강의 시간)
            # 선수 과목을 다 들어야 다음 과목을 들을 수 있으므로 큰 값을 저장함
            result[lec] = max(result[lec], result[now] + time[lec])
            indegree[lec] -= 1      # 진입 차수 1 빼기
            
            # 새로 진입차수가 0이 되는 강의(노드) 큐에 넣기
            if indegree[lec] == 0:
                q.append(lec)

    # 위상 정렬 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

# 위상 정렬 수행
topology_sort()