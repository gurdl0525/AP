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
    visited = [False] * N

    dfs(0, visited, N)


def dfs(_v: int, _visited: list, _N: int):
    if _v == _N:
        for i, v in enumerate(_visited):
            if v:
                print(i + 1, end=' ')
        return
    _visited[_v] = True
    dfs(_v + 1, _visited, _N)
    print('\n', end='', sep='')
    _visited[_v] = False
    dfs(_v + 1, _visited, _N)


if __name__ == '__main__':
    solution()
