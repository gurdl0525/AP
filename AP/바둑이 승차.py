# 바둑이 승차(DFS)

# input
# 259 5
# 81
# 58
# 42
# 33
# 61

# output
# 242

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    C, N = list(map(int, input().split()))
    badook = [int(input()) for _ in range(N)]
    visited = [False] * N

    badook.sort()
    badook.reverse()

    print(dfs(badook, 0, visited, C, N))


def dfs(_badook: list, _v: int, _visited: list, _C: int, _N: int):
    if _v == _N:
        sum = 0
        for i, v in enumerate(_visited):
            if v:
                sum += _badook[i]
        return sum

    _visited[_v] = True

    sum = dfs(_badook, _v + 1, _visited, _C, _N)

    if sum is not None:
        return sum

    _visited[_v] = False
    return dfs(_badook, _v + 1, _visited, _C, _N)


if __name__ == '__main__':
    solution()
