# 제곱 ㄴㄴ 수 (1016)


# 에라토스테네스의 체 : (ex) 2를 통해 4, 6, 8, 10, 12 제거 3을 통해 6, 9, 12 제거
def solution():
    min, max = map(int, input().split())

    cnt: int = max - min + 1  # 15 ~ 15 범위 일때 1을 만들기 위함

    check = [False] * cnt

    i: int = 2  # 1^2은 1이므로 2부터 시작
    while i * i <= max:
        pow: int = i * i  # i의 제곱수
        j: int = min // pow if min % pow == 0 else min // pow + 1  # i가 2고 min이 15일 때 4

        while j * pow <= max:  # 범위 안에 수인지 판별
            sqrt = j * pow - min  # index 찾기

            if not check[sqrt]:  # 이미 제거한 수 인지 판별
                check[sqrt] = True
                cnt -= 1
            j += 1
        i += 1

    print(cnt)
