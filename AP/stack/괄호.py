# 괄호

# input
# 첫번쨰 줄 : 입렫 테이터의 수를 나타내는 정수 T
# 괄호 문자열이 주어지며 길이는 2이상 50이하이다.

# output
# 괄호 문자열이 올바른 괄호 문자면 Yes 아니면 No를 선택하면 된다.

# ----------------------------------------------------------------------------------------------------------------------

def solution():
    T = int(input())
    inp = [input() for _ in range(T)]

    result = [True for _ in range(T)]

    for i, v in enumerate(inp):
        stack = []
        for s in inp[i]:
            if s == '(':
                stack.append(s)
            elif s == ')' and len(stack) > 0:
                stack.pop()
            else:
                result[i] = False
        if len(stack) != 0:
            result[i] = False

    print(* result, sep='\n')


if __name__ == '__main__':
    solution()