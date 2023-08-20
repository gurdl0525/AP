ip = int(input())


def getOne(n):
    if n == 1:
        return 0

    ls = [0]

    for i in range(ip + 1)[:1:-1]:
        print(i)
