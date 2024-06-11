# 합이 같은 부분집합(DFS: 아마존 인터뷰)

# input
# 6
# 1 3 5 6 7 10

# output
# YES

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    N = int(input())
    ls = [int(v) for v in input().split()]
    visited = [False] * N

    print('YES' if dfs(ls, 0, visited, N, False) else 'NO')


def dfs(_ls: list, _v: int, _visited: list, _N: int, _success: bool):
    if _success:
        return _success

    if _v == _N + 1:
        plus, minus = 0, 0

        for i, v in enumerate(_visited):
            if v:
                plus += _ls[i]
            else:
                minus += _ls[i]

        if plus == minus:
            _success = True

        return _success

    _visited[_v] = True
    _success = dfs(_ls, _v + 1, _visited, _N, _success)
    _visited[_v] = False
    return dfs(_ls, _v + 1, _visited, _N, _success)


if __name__ == '__main__':
    solution()
