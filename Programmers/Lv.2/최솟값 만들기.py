# 최솟값 만들기

def solution(A,B):
    answer = 0
    
    if min(A) < min(B):
        A.sort()
        B.sort(reverse=True)
    else:
        A.sort(reverse=True)
        B.sort()
        
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer