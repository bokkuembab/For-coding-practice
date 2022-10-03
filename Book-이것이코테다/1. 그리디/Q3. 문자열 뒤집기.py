# 그리디 알고리즘 기출문제 Q3. 문자열 뒤집기

# 문자열 입력 받기
s = list(map(int, input()))

# 개수가 더 많은 수 찾기
t = 1 if s.count(1) >= s.count(0) else 0

# 뒤집을 횟수 초기화 (첫번째 수가 개수가 더 많은 수가 아니라면 1로 초기화)
res = 1 if s[0] != t else 0

# 연속되는 수가 다르고, 개수가 많은 수가 아니라면 뒤집기 횟수 1 증가
for i in range(1, len(s) - 1):
    if s[i] != s[i + 1] and s[i + 1] != t:
        res += 1

# 결과 출력
print(res)