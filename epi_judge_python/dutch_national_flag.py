import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def bruteforce(pivot_index: int, A: List[int]) -> List[int]:
    pivot = A[pivot_index]
    L, E, G = [], [], []
    for i in A:
        if i == pivot:
            E.append(i)
        elif i < pivot:
            L.append(i)
        else:
            G.append(i)
    return L + E + G

def optimal(pivot_index: int, A: List[int]) -> None:
    pivot, s, e, l = A[pivot_index], 0, 0, len(A)
    while e < l:
        if A[e] < pivot:
            A[s], A[e] = A[e], A[s]
            s, e = s + 1, e + 1
        elif A[e] > pivot:
            l -= 1
            A[e], A[l] = A[l], A[e]
        else:
            e += 1
    return


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    optimal(pivot_index, A)
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
