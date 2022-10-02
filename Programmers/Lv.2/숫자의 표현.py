# 숫자의 표현

def solution(n):
    answer = 0
    
    # 최대로 더할 수 있는 수의 조합은 중간값끼리의 합이므로
    # (중간값 + 1)까지 확인함
    for i in range(1, n // 2 + 1):
        sum = 0
        for j in range(i, n // 2 + 2):
            sum += j
            if sum >= n:
                break
        if sum == n:
            answer += 1
    
    return answer + 1       # 본인만 더하는 경우 포함