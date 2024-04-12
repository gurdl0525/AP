# 순열 (1115)

# input
# 5
# 2 0 1 4 3

# output
# 2

def perfectPermutation(_A: list, _B: list, _N: int):
    if _B[0] != 0:
        return False

    i = 1
    while True:
        if 1 <= i <= _N - 1:
            break
        if _B[i] != _A[_B[i - 1]]:
            return False
        i += 1

    return True


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    print(perfectPermutation(P, [0, 2, 1], N))
