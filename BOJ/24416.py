ip = int(input())


def fibonacci(n):
    f = [0] * (n + 1)

    f[1], f[2] = 1, 1

    for i in range(n + 1)[3:n + 1]:
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
