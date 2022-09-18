# 이진 탐색 문제 - 떡볶이 떡 만들기
# 파라매트릭 서치 문제 유형: 최적화 문제를 결정 문제로 바꾸어 해결하는 방법
# 보통 파라메트릭 서치 유형은 이진 탐색을 이용해 해결함
# 파라메트릭의 이진 탐색은 반복문을 이용해 구현하면 더 간결함

# 떡의 개수, 요청한 떡의 길이 입력 받기
n, m = map(int, input().split())

# 떡의 개별 높이 입력 받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점, 끝점 설정
start, end = 0, max(array)

# 이진 탐색 수행 (반복적)
result = 0
while start <= end:

    # 중간값 설정
    mid = (start + end) // 2
    total = 0

    for ddeok in array:
        # 잘랐을 때의 남은 떡의 길이 계산
        if ddeok > mid:
            total += ddeok - mid

    # 남은 떡의 총합이 요청한 길이보다 작은 경우
    # 자르는 높이를 짧게 하기 (왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 남은 떡의 총합이 요청한 길이보다 큰 경우
    # 자르는 높이를 길게 하기 (오른쪽 탐색)
    else:
        result = mid        # 최대한 덜 잘랐을 때가 정답이므로, result에 기록
        start = mid + 1

# 결과값 출력
print(result)
