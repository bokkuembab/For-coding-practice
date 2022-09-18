# 이진 탐색 문제 - 부품 찾기

# 입력 받기
n = int(input())
store = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

# 가게 부품 정렬시킴
store.sort()

# 이진 탐색 구현
def binary_search(array, target, start, end):

    while start <= end:

        # 중간값 설정
        mid = (start + end) // 2

        # 찾는 값을 찾으면, True 출력
        if array[mid] == target:
            return True
        # 찾는 값이 중간값보다 작으면, 왼쪽 탐색
        elif target < array[mid]:
            end = mid - 1
        # 찾는 값이 중간값보다 크면, 오른쪽 탐색
        else:
            start = mid + 1

    # 찾는 값을 못 찾은 경우, False 출력
    return False

# 손님이 찾는 리스트 요소들 반복 탐색
for item in guest:
    
    # 찾는 값이 있는 경우
    if binary_search(store, item, 0, n - 1):
        print("yes", end=' ')
    # 찾는 값이 없는 경우
    else:
        print("no", end=' ')
