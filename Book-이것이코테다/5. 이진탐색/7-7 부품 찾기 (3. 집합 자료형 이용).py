# 집합 자료형 이용 - 부품 찾기
# 굳이 순서 중요 X, 단순히 특정한 수가 한 번이라도 등장했는지를 검사하면 됨 -> 집합 자료형 이용
# set() 함수는 집합 자료형을 초기화할 때 사용

# 가게 부품 수 입력 받기
n = int(input())

# 집합 자료형으로 부품 번호들 입력 받기
store = set(map(int, input().split()))

# 손님 요청 부품 수, 번호 입력 받기
m = int(input())
guest = list(map(int, input().split()))

# 요청 부품 존재하는지 하나씩 확인
for item in guest:

    # 존재하면, yes 출력
    if item in store:
        print("yes", end=' ')
    # 존재하지 않으면, no 출력
    else:
        print("no", end=' ')