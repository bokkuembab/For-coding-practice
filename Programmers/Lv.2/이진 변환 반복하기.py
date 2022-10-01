# 이진 변환 반복하기

def binary_trans(s):
    ct = s.count('0')
    tr = bin(len(s.replace('0', '')))
    return ct, str(tr[2:])

def solution(s):
    ans = [0, 0]
    while s != '1':
        ct, s = binary_trans(s)
        ans[0] += 1  
        ans[1] += ct

    return ans