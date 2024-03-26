# 동전교환
import ctypes


# input
# 3
# 1 2 5
# 15

# output
# 3

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    N = int(input())
    coins = list(map(int, input().split()))

    if N != len(coins):
        return

    M = int(input())

    coins.reverse()

    for c in coins:
        dfs(coins, 0, 0, M, c)

    print(_min)


def dfs(_coins: list, _depth: int, _len: int, _now: int, _c: int):

    global _min

    _len += 1
    _now -= _c

    if _now < 0 or _len > _min:
        return

    if _now == 0:
        if _min > _len:
            _min = _len
        return

    for c in _coins:
        dfs(_coins, _depth + 1, _len, _now, c)


if __name__ == '__main__':
    _min = 101
    solution()
