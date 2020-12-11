from test_framework import generic_test

def multiply(x: int, y: int) -> int:
    def add(x: int, y: int) -> int:
        while y:
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x
    result = 0
    while x:
        if x & 1:
            result = add(result, y)
        x, y = x >> 1, y << 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
