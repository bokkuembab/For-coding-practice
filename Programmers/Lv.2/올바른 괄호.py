# 올바른 괄호

def solution(s):
    ans = False
    t = 0
    
    for i in s:
        # t의 값이 음수이면 반복 종료
        if t < 0:
            ans = False
            break
        if i == '(':
            t += 1
        elif i == ')':
            t -= 1
    # 열린, 닫힌 괄호의 개수가 같아야 true 출력
    if t == 0:
        ans = True
            
    return ans