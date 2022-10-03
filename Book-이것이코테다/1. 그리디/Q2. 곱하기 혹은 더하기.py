# 그리디 알고리즘 기출문제 Q2. 곱하기 혹은 더하기

# 문자열 입력 받기
s = input()

# 결과를 문자열의 첫번째 숫자로 초기화
res = int(s[0])

# 숫자 하나씩 확인
for i in range(1, len(s)):

    # 문자열의 숫자 저장
    n = int(s[i])

    # 곱하거나 더한 수 중, 큰 값 저장
    res = max(res * n, res + n)

print(res)