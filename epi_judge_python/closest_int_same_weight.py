from test_framework import generic_test

# solution taken from stack overflow
def closest_int_same_bit_count(x: int) -> int:
    s = x & ~(x - 1)
    ns = ~x & (x + 1)
    if ns > s:
        x |= ns
        x ^= ns >> 1
    else:
        x ^= s
        x |= s >> 1
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
