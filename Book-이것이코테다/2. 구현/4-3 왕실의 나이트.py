### 구현 예제 - 왕실의 나이트 ###

# 위치 입력 받기
L = input()

# 행, 열 분할해 숫자로 저장
data = [ord(L[0]) - ord('a') + 1, int(L[1])]

cMin, cMax = 1, 8
res = 0

# 이동 가능한 8가지 경우
steps = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

for s in steps:
    tx = data[0] + s[0]
    ty = data[1] + s[1]

    # 이동 불가능할 경우 무시
    if tx < cMin or tx > cMax or ty < cMin or ty > cMax:
        continue

    # 경우의 수 더함
    res += 1

# 결과 출력
print(res)