# 부분집합 구하기(DFS)

# input
# 3 2

# output
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 9

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    N, M = map(int, input().split())

    stack = []
    for i in range(1, N + 1):
        stack.append(i)
        dfs(stack, 1,  N, M)
        stack.pop()

    print(s)


def dfs(_I: list, _D: int,  _N: int, _M: int):
    if _D == _M:
        global s
        s += 1
        print(*_I, end='\n', sep=' ')
        return

    for i in range(1, _N + 1):
        _I.append(i)
        dfs(_I, _D + 1, _N, _M)
        _I.pop()


if __name__ == '__main__':
    s = 0
    solution()
