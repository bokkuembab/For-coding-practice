# 정렬 문제 - 위에서 아래로
# 내림차순으로 정렬 후, 결과를 공백으로 구분해 출력

# 입력 받기
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리 이용해 정렬 수행
array = sorted(array, reverse = True)

# 정렬된 리스트 출력
for i in array:
    print(i, end=' ')