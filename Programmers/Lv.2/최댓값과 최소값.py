# 최댓값과 최소값

def solution(s):
    array = list(map(int, s.split()))
    result = str(min(array)) + ' ' + str(max(array))
    
    return result