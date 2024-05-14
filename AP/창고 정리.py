# 창고 정리

# input
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50

# output
# 20

if __name__ == '__main__':
    L = int(input())
    n = list(map(int, input().split()))
    M = int(input())

    for _ in range(M):
        n[n.index(min(n))] += 1
        n[n.index(max(n))] -= 1

    print(max(n) - min(n))
