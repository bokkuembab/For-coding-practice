# 정렬 문제 - 성적이 낮은 순서로 학생 출력하기

# 입력 받기
n = int(input())

# 이름과 성적 구분해 입력 받기
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 키를 이용해 점수를 기준으로 정렬
# lambda 함수로 튜플을 student로 받아 점수를 키로 설정
array = sorted(array, key=lambda student: student[1])

# 정렬된 학생 이름 출력
for student in array:
    print(student[0], end=' ')