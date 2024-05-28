# 단어 정렬

# 1. 리스트 요소 길이순 정렬
# 2. 사전순 정렬

# input
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

# output
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate

if __name__ == '__main__':
    print(*sorted(set([input() for _ in range(int(input()))]), key=lambda x: (len(x), x)), sep='\n')
