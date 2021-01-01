from typing import List
import bisect

from test_framework import generic_test

def optimal(A: List[int], k: int) -> int:
    L, U, result = 0, len(A) - 1, -1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < k:
            L += 1
            continue
        if A[M] == k:
            result = M
        U -= 1
    return result
            
        

def naive(A: List[int], k: int) -> int:
    L, M, U = 0, -1, len(A) - 1
    if not A or k < A[0] or k > A[-1]:
        return -1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < k:
            L = M + 1
        elif A[M] == k:
            break
        else:
            U = M - 1
    if A[M] == k:
        while M > 0:
            if A[M - 1] == A[M]:
                M -= 1
            else:
                break
    else:
        return - 1
    return M

def bisect_solution(A: List[int], k: int) -> int:
    result = bisect.bisect_left(A, k)
    return -1 if result == len(A) or k < A[result] else result
        

def search_first_of_k(A: List[int], k: int) -> int:
    return optimal(A, k)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
