# 정다면체

# 두 개의 정 N면채와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장
# 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# input
# 첫 번째 줄에는 자연수 N과 M이 주어집니다.
# N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

# output
# 첫 번째 줄에 답을 출력합니다.

# example
# in : 4 6
# out : 5 6 7

# ----------------------------------------------------------------------------------------------------------------------

# if input is 4 -> 1, 2, 3, 4
# if input is 6 -> 1, 2, 3, 4, 5, 6

# when
#   2 -> (1, 1)
#   3 -> (1, 2), (2, 1)
#   4 -> (1, 3), (2, 2), (3, 1)
#   5 -> (1, 4), (2, 3), (3, 2), (4, 1)
#   6 -> (1, 5), (2, 4), (3, 3), (4, 2)
#   7 -> (1, 6), (2, 5), (3, 4), (4, 3)
#   8 -> (2, 6), (3, 5), (4, 4)
#   9 -> (3, 6), (4, 5)
#   10 -> (4, 6)

def solution():
    n, m = map(int, input().split())

    bigger = max(n, m)
    smaller = n if n != bigger else m

    pivot = (n + m + 2) / 2

    div = (bigger - smaller)

    if div != 0:
        div = int(div / 2)
        result = ""
        for i in range(int(pivot - div), int(pivot + div) + 1):
            result += (str(i) + " ")
        print(result)
    else:
        print(int(pivot))


def solution_v2():
    n, m = map(int, input().split())

    result = ""
    for i in range(min(n, m) + 1, max(n, m) + 2):
        result += (str(i) + " ")

    print(result)



