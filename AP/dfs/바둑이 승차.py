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
        tmp = 0
        for i, v in enumerate(_visited):
            if v:
                tmp += _badook[i]
        if tmp <= _C:
            return tmp
        return None

    _visited[_v] = True

    tmp = dfs(_badook, _v + 1, _visited, _C, _N)

    if tmp is not None:
        return tmp

    _visited[_v] = False
    return dfs(_badook, _v + 1, _visited, _C, _N)


if __name__ == '__main__':
    solution()


def DFS(i, s, tsum):
    global m
    if s + (sum(a) - tsum) < m:
        return
    if s > c:
        return
    if n == i:
        if m <= s:
            m = s
    else:
        DFS(i + 1, s + a[i], tsum + a[i])
        DFS(i + 1, s, tsum + a[i])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = []
    m = 0
    for i in range(n):
        a.append(int(input()))
    DFS(0, 0, 0)
    print(m)
