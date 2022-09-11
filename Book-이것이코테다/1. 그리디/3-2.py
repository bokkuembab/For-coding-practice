### 그리디 예제 - 큰 수의 법칙 ###

N, M, K = map(int, input().split())
d = list(map(int,input().split()))

s = M // (K + 1)
r = M % (K + 1)
n1 = max(d)
d.remove(n1)
n2 = max(d)

print(s * (n1 * K + n2) + r * n1)