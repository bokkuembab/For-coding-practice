# 데이터 입력 받기
N, M = map(int, input().split())        # 맵 크기
r, c, d = map(int, input().split())     # 초기 위치: (r,c), 방향: d
maps = []
for _ in range(N):                      # 맵 육지(0) or 바다(1) 입력
    maps.append(list(map(int, input().split())))

# 방문 체크 배열 생성
check = [[0] * M for _ in range(N)]
check[r][c] = 1                         # 초기 위치 방문 체크

# d의 인덱스 기준 이동
# 0: 북, 1: 동, 2: 남, 3: 서
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 왼쪽으로 회전 함수
def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3

# 이동 시작
turns = 0       # 회전 횟수

while True:
    # 왼쪽으로 회전시키기
    turn_left()
    tr = r + move[d][0]
    tc = c + move[d][1]

    # 가보지 않은 곳이고, 육지이면 이동
    if check[tr][tc] == 0 and maps[tr][tc] == 0:
        r, c = tr, tc
        check[r][c] = 1
        turns = 0
        continue
    # 회전한 후, 바라보는 곳이 가본 곳이거나 바다인 경우
    else:
        turns += 1

    # 네 방향 모두 가본 곳인 경우
    if turns == 4:
        tr = r - move[d][0]
        tc = c - move[d][1]
        # 뒤가 바다인 경우 전체 종료
        if maps[tr][tc] == 1:
            break
        # 뒤가 육지인 경우 이동
        else:
            r, c = tr, tc
            turns = 0

# 가본 곳 세기
res = 0
for i in range(N):
    res += check[i].count(1)

# 결과 출력
print(res)
    