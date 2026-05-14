import re


def solution(expression):
    answer = 0
    expressions = re.split(r'(\+|\-|\*)', expression)

    for i in range(len(expressions)):
        if expressions[i].isdigit():
            expressions[i] = int(expressions[i])
    first_multiply_second_plus = int(abs(minus(plus(multiply(expressions)))[-1]))
    answer=max(first_multiply_second_plus,answer)
    first_multiply_second_minus = int(abs(plus(minus(multiply(expressions)))[-1]))
    answer = max(first_multiply_second_minus, answer)
    first_plus_second_multiply = int(abs(minus(multiply(plus(expressions)))[-1]))
    answer = max(first_plus_second_multiply, answer)
    first_plus_second_minus = int(abs(multiply(minus(plus(expressions)))[-1]))
    answer=max(first_plus_second_minus,answer)
    first_minus_second_multiply = int(abs(plus(multiply(minus(expressions)))[-1]))
    answer=max(first_minus_second_multiply,answer)
    first_minus_second_plus = int(abs(multiply(plus(minus(expressions)))[-1]))
    answer = max(first_minus_second_plus, answer)
    return answer


def multiply(expressions):
    stack = []
    i = 0
    while i < len(expressions):
        if expressions[i] == "*":
            stack[-1] *= expressions[i + 1]
            i += 2
        else:
            stack.append(expressions[i])
            i += 1
    return stack


def plus(expressions):
    stack = []
    i = 0
    while i < len(expressions):
        if expressions[i] == "+":
            stack[-1] += expressions[i + 1]
            i += 2
        else:
            stack.append(expressions[i])
            i += 1
    return stack


def minus(expressions):
    stack = []
    i = 0
    while i < len(expressions):
        if expressions[i] == "-":
            stack[-1] -= expressions[i + 1]
            i += 2
        else:
            stack.append(expressions[i])
            i += 1
    return stack


expression = "100-200*300-500+20"
print(solution(expression))
