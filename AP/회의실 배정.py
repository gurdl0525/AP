# 회의실 배정(그리디)

# input
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# output
# 3

# (2, 3), (3, 5), (5, 7) 회의실을 이용할 수 있다.

# if __name__ == '__main__':
#     n = int(input())
#     meet = sorted([list(map(int, input().split())) for i in range(n)], key=lambda t: t[1])
#
#     sets = set()
#     count = 0
#
#     for i in meet:
#         tmp = set(range(i[1])[i[0]:])
#
#         if sets:
#             if sets.intersection(tmp):
#                 continue
#             else:
#                 count += 1
#                 sets.update(tmp)
#         else:
#             count += 1
#             sets.update(tmp)
#
#     print(count)

if __name__ == '__main__':
    n = int(input())
    meet = sorted([list(map(int, input().split())) for i in range(n)], key=lambda t: t[1])

    start, end, count = 0, 0, 0

    for i in meet:

        if i[1] < start or end <= i[0]:
            start = i[0]
            end = i[1]
            count += 1

    print(count)
