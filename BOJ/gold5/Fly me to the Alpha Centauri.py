# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

# input
# 3
# 0 3
# 1 5
# 45 50

# output
# 3
# 3
# 4

if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(T):
        x, y = map(int, input().split())
        distance = y - x

        if distance <= 3:
            res.append(distance)
            continue

        square = int(distance ** (1 / 2))
        square_pow = square ** 2

        if distance == square_pow:
            res.append((square * 2) - 1)

        elif square_pow < distance <= square_pow + square:
            res.append(square * 2)
            
        else:
            res.append((square * 2) + 1)

        # elif square + square_pow < distance:
        #     res.append((square * 2) + 1)

    print(*res, sep='\n')
