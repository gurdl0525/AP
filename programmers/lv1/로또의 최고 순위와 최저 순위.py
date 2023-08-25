# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
def solution(lottos: list, win_nums: list):
    win_cnt, def_cnt = 1, 1
    for lotto in lottos:
        if lotto not in win_nums:
            def_cnt += 1
            if lotto != 0:
                win_cnt += 1

    return [win_cnt - 1 if win_cnt > 6 else win_cnt, def_cnt - 1 if def_cnt > 6 else def_cnt]
