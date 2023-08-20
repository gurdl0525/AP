# 2018 KAKAO BLIND RECRUITMENT
def solution(dartResult):

    stack = [0]

    for index, dart in enumerate(dartResult):

        try:
            numDart = int(dart)

            if index != 0:

                try:
                    leftDart = int(dartResult[index - 1])
                    stack.pop(-1)
                    stack.append(leftDart * 10 + numDart)

                except ValueError:
                    stack.append(numDart)

            else:
                stack.append(numDart)

        except ValueError:

            if dart == '*':
                stack[-2] *= 2
                stack[-1] *= 2

            elif dart == '#':
                stack[-1] *= -1

            elif dart == 'D':
                stack[-1] *= stack[-1]

            elif dart == 'T':
                stack[-1] *= stack[-1] * stack[-1]

            else:
                continue

    return sum(stack)
