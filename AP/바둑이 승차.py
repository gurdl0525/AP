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

    print(dfs(badook, 0, visited, C,  N, 0))


def dfs(_badook: list, _v: int, _visited: list, _C: int, _N: int, _max: int):
    if _v == _N:
        sum = 0
        for i, v in enumerate(_visited):
            if v:
                sum += _badook[i]
        if _max < sum <= _C:
            _max = sum
        return _max

    _visited[_v] = True
    _max = dfs(_badook, _v + 1, _visited, _C, _N, _max)

    _visited[_v] = False
    return dfs(_badook, _v + 1, _visited, _C, _N, _max)


if __name__ == '__main__':
    solution()
