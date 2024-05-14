# 역수열(그리디)

# input
# 8
# 5 3 4 0 2 1 1 0

# output
# 4 8 6 2 5 1 3 7

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = []

    for i, v in enumerate(numbers[::-1]):
        ans.insert(v, N - i)

    print(*ans, sep=' ')

