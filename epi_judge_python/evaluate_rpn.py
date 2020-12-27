from test_framework import generic_test


def evaluate(expression: str) -> int:
    intermediate_results = []
    DELIMETER = ','
    OPERATORS = {'+': lambda y, x: x + y, '-': lambda y, x: x - y,
                 '*': lambda y, x: x * y, '/': lambda y, x: int(x / y)
                 }
    for token in expression.split(DELIMETER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
