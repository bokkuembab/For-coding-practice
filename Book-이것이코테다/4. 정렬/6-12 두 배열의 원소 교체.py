# 정렬 문제 - 두 배열의 원소 교체

# 두 배열의 원소 개수, 바꿔치기 연산의 최대값 입력 받기
n, k = map(int, input().split())

# 두 배열의 원소들 입력 받기
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

# 두 배열 정렬하기
# a1은 오름차순, a2는 내림차순
a1.sort()
a2.sort(reverse=True)

# k번 동안 큰 수 확인 후, 바꿔치기
for i in range(k):
    
    # a1의 최소값보다 a2의 최대값이 더 크면, 교체
    if a1[i] < a2[i]:
        a1[i], a2[i] = a2[i], a1[i]
    # a1의 최소값이 a2의 최대값보다 크거나 같을 때, 반복문 탈출
    else:
        break

# 결과값 출력
print(sum(a1))