### 구현 예제 - 1. 상하좌우 ###

# N, plan 입력
from tkinter import X


N = int(input())
plan = input().split()

# 변수 초기화
x, y = 1, 1
cMin, cMax = 1, N
option = ['L', 'R', 'U', 'D']
movX = [-1, 1, 0, 0]
movY = [0, 0, -1, 1]

# 하나씩 확인
for p in plan:
    # 문자에 따라 이동
    for i in range(len(option)):
        if p == option[i]:
            tx = x + movX[i]
            ty = y + movY[i]
    
    # 이동 불가능하면 무시
    if tx < cMin or tx > cMax or ty < cMin or ty > cMax:
        continue

    x, y = tx, ty

print(y, x)