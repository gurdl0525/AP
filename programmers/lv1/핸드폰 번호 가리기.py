def solution(phone_number):

    answer = phone_number[-4:]

    answer = answer.rjust(len(phone_number), '*')
    return answer
