from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    S = list()
    sign = ''
    if x < 0:
        x, sign = -x, '-'
    while True:
        print(x)
        S.append(chr(ord('0') + (x % 10)))
        x //= 10
        if not x:
            break
    return sign + ''.join(reversed(S))


def string_to_int(s: str) -> int:
    start = 1 if ord(s[0]) < ord('0') else 0
    for c in range(start, len(s)):
        result = result * 10 + (ord(s[c]) - ord('0'))
    return -result if s[0] == '-' else result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
