def is_correct_parenthesis(string):
    new = []
    for x in string:
        if x=='(':
            new.append(x)
        else:
            if not new:
                return False
            new.pop()

    if len(new)==0:
        return True
    return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))