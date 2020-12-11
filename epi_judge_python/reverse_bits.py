from test_framework import generic_test


def reverse_bits(x: int) -> int:
    def swap_bits(x, i, j):
            if (x >> i) & 1 != (x >> j) & 1:
                x ^= (1 << i) | (1 << j)
            return x
    for i in range(0, 32):
        x = swap_bits(x, i, 63 - i)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
