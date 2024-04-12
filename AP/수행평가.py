# 최대점수 구하기(DFS)

# input
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

# output
# 41

# ---------------------------------------------------------------------------------------------------------------------

def solution():
    NM = list(map(int, input().split()))

    N, M = NM[0], NM[1]

    visited = [False] * N
    problem_score = []

    for _ in range(N):
        tmp = list(map(int, input().split()))
        problem_score.append([tmp[0], tmp[1]])

    dfs(0, N, visited, M, problem_score, 0)


def dfs(_I: int, _N: int, _visited: list, _T: int, _problem_score: list, _S: int):  # _I 인덱스, _D 뎁스, _T 시간, _M 종 시간

    if _I == _N:

        for i, v in enumerate(_visited):
            if v:
                _S += _problem_score[i][0]
                _T -= _problem_score[i][1]

        global _max

        if _max < _S and _T >= 0:
            _max = _S

        return

    _visited[_I] = True
    dfs(_I + 1, _N, _visited, _T, _problem_score, _S)
    _visited[_I] = False
    dfs(_I + 1, _N, _visited, _T, _problem_score, _S)


if __name__ == '__main__':
    _max = 0
    solution()
    print(_max)
