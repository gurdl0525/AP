import re


def solution(my_string):
    return sum(list(map(int, re.findall('\d+', my_string))))
