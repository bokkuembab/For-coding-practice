### 그리디 예제 - 1이 될 때까지 ###

N, K = map(int, input().split())
res = 0

while N >= K:
    if N % K != 0:
        res += N % K
        N -= N % K
    else:
        res += 1
        N //= K

if N == 1:
    print(res)
else:
    print(res + N - 1)