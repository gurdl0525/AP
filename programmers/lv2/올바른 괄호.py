def solution(s):
    count = 0
    for st in s:

        if st == '(':
            count += 1

        if st == ')':
            count -= 1

            if count < 0:
                return False

    return True if count == 0 else False
