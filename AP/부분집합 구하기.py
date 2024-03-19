# 부분집합 구하기(DFS)

# input
# 3

# output
# 1 2 3
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    N = int(input())
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
