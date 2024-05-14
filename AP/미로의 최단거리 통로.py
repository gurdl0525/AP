# 미로의 최단거리 통로 (BFS 활용)

# input
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0

# output
# 12

def bfs(_x: int, _y: int, _m: int, _M: list):
    global m
    _M[_x][_y] = 1

    if _x == _y == 6:
        if m < 0 or _m < m:
            m = _m
        return

    p_x, p_y, m_x, m_y = _x + 1, _y + 1, _x - 1, _y - 1

    if p_x < 7 and _M[p_x][_y] != 1:
        bfs(p_x, _y, _m + 1, _M[:])
    if p_y < 7 and _M[_x][p_y] != 1:
        bfs(_x, p_y, _m + 1, _M[:])
    if 0 <= m_y and _M[_x][m_y] != 1:
        bfs(_x, m_y, _m + 1, _M[:])
    if 0 <= m_x and _M[m_x][_y] != 1:
        bfs(m_x, _y, _m + 1, _M[:])


if __name__ == '__main__':
    M, m = [], -1
    for _ in range(7):
        M.append(list(map(int, input().rstrip().split())))
    bfs(0, 0, 0, M[:])
    print(m)
