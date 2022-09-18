# 계수 정렬 - 부품 찾기
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 후,
# 리스트의 인덱스에 직접 접근해 특정 번호의 부품이 매장에 존재하는지 확인

# 가게 부품 개수 입력 받기
n = int(input())

# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 만듬
store = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아 기록
for i in input().split():
    store[int(i)] = 1

# 손님이 요청한 부품 개수와 번호 입력 받기
m = int(input())
guest = list(map(int, input().split()))

# 손님이 요청한 부품 있는지 하나씩 확인
for item in guest:

    # 보유하고 있다면, yes 출력
    if store[item] == 1:
        print("yes", end=' ')
    # 보유하지 않고 있다면, no 출력
    else:
        print("no", end=' ')