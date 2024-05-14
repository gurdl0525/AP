# 씨름 선수(그리디)

# input
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

# output
# 3

# (185, 65), (180, 70), (170, 72)

if __name__ == '__main__':
    N = int(input())
    hw = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda h: h[0], reverse=True)
    _max, count = 0, 0

    for i in hw:
        if _max < i[1]:
            count += 1
            _max = i[1]

    print(count)
