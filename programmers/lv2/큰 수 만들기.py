def solution(number, k):
    if min(number) == '9':  # 가장 작은 수가 9일때 length - k 만큼 9999...9보내기
        return ''.join(['9' for _ in range(len(number) - k)])

    number = list(number)

    stack = []

    for n in number:

        while k > 0 and stack and stack[-1] < n:  # stack 존재하고 k가 0보다 크며 stack의 마지막 값이 n보다 작을 때
            k -= 1
            stack.pop(-1)
        stack.append(n)

    if k != 0:  # 만약 for이 끝났지만 k가 0보다 큰경우 (ex: number = 54321, k = 2)
        stack = stack[:-k]  # stack을 슬라이싱 (ex: stack = 54321 -> 543)

    return ''.join(stack)
