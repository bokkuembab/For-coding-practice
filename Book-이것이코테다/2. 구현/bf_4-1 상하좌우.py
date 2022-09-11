### 구현 예제 - 1. 상하좌우 ###

# N, plan 입력
N = int(input())
plan = input().split()

# 변수 초기화
x, y = 1, 1
cMin, cMax = 1, N

# 하나씩 꺼냄
for p in plan:
    # 문자에 따라 이동
    if p == 'R':
        tx = x + 1
        ty = y
    elif p == 'L':
        tx = x - 1
        ty = y
    elif p == 'D':
        ty = y + 1
        tx = x
    elif p == 'U':
        ty = y - 1
        tx = x
    
    # 이동 불가능하면 무시
    if tx < cMin or tx > cMax or ty < cMin or ty > cMax:
        continue
    
    # 이동
    x, y = tx, ty

print(y, x)