from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    if not s:
        return False
    D = {'{' : '}',
         '(' : ')',
         '[' : ']'}
    S = list()
    
    for i in range(len(s)):
        if s[i] in D:
            S.append(s[i])
        elif not (S and D[S.pop()] == s[i]):
            return False
    return not S


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
