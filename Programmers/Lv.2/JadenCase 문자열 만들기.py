# JadenCase 문자열 만들기

def solution(s):
    arr = list(s.split(' '))
    ans = []
    
    for i in range(len(arr)):
        ans.append(arr[i][:1].upper() + arr[i][1:].lower())
    ans = ' '.join(ans)
    
    return ans