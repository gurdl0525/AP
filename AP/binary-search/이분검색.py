# 이분검색

# input
# 8 32
# 23 87 65 12 57 32 99 81

# output
# 3

if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    result = 1

    while True:
        middle = int(len(numbers) / 2)

        if numbers[middle] == M:
            result += middle
            break

        elif numbers[middle] < M:
            numbers = numbers[middle::]
            result += middle

        else:
            numbers = numbers[:middle:]

    print(result)
