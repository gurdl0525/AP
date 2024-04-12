# 휴가(삼성 SW역량평가 기출문제 : DFS활용)

# input
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10

# output
# 60

# ---------------------------------------------------------------------------------------------------------------------


def solution():
    N = int(input())
    TP = []

    for _ in range(N):
        TP.append(list(map(int, input().split())))

    _visited = [False] * N

    dfs(0, N, _visited, TP)

    print(_max)


def dfs(_Deps: int, _N: int, _visited: list, _TP: list):
    global _max

    if _Deps == _N:
        M = 0
        for i, v in enumerate(_visited):
            if v:
                M += _TP[i][1]
                for i2 in range(_TP[i][0]):
                    if len(_visited) <= i + i2:
                        M -= _TP[i][1]
                        break
                    _visited[i + i2] = False

        if M > _max:
            _max = M

        return

    _visited[_Deps] = True
    tmp = _visited.copy()
    dfs(_Deps + 1, _N, _visited, _TP)

    _visited = tmp.copy()
    _visited[_Deps] = False
    dfs(_Deps + 1, _N, _visited, _TP)


if __name__ == '__main__':
    _max = 0
    solution()
