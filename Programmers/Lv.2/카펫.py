# 카펫

def solution(brown, yellow):
    answer = []

    # w: yellow 영역의 너비, h: yellow 영역의 높이
    # w + h = (brown - 4) / 2
    # w * h = yellow
    # 둘을 연립하여 이차방정식의 해를 구하면 됨
    # 구하려는 것: [w + 2, h + 2]
    # a + b = w + h + 4 = (brown - 4) / 2 + 4 = p
    # ab = (w + 2) * (h + 2) = wh + 2(w + h) + 4 = yellow + 2 * p + 4 = q
    # x^2 -px + q = 0 의 해를 근의 공식으로 구하면 됨
    # h <= w 이므로 루트 값을 더해준 것이 w, 빼준 것이 h가 됨
    p = (brown - 4) * 0.5 + 4
    q = yellow + 2 * p - 4
    p *= -1

    k = (p ** 2 - 4 * q) ** 0.5
    answer.append(int((-1 * p + k) * 0.5))
    answer.append(int((-1 * p - k) * 0.5))


    return answer