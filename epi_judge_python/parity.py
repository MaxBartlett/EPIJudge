from test_framework import generic_test

def variant(x: int) -> int:
    def rightpropagate(x: int) -> int:
        return x | x - 1
    
    def modpowertwo(x: int, y: int) -> int:
        return x & y - 1
    
    def ispowertwo(x: int) -> bool:
        return x & x - 1 == 0

    return ispowertwo(x)
    

def bruteforce(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def erasebits(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

def parity(x: int) -> int:
    return bruteforce(x)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
