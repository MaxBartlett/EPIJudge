from test_framework import generic_test
from collections import Counter

def counter(letter_text: str, magazine_text: str) -> bool:
    magazine_counter = Counter(list(magazine_text))
    letter_counter = Counter(list(letter_text))
    return not letter_counter - magazine_counter

def magazine_counter(letter_text: str, magazine_text: str) -> bool:
    magazine_counter = Counter(list(magazine_text))
    for c in letter_text:
        if c not in magazine_counter:
            return False
        magazine_counter[c] -= 1
        if magazine_counter[c] < 0:
            return False
    return True

def letter_counter(letter_text: str, magazine_text: str) -> bool:
    letter_counter = Counter(list(letter_text))
    for c in magazine_text:
        if c in letter_counter:
            letter_counter[c] -= 1
            if letter_counter[c] == 0:
                del letter_counter[c]
                if not letter_counter:
                    return True
    return not letter_counter
    

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    return counter(letter_text, magazine_text)
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
