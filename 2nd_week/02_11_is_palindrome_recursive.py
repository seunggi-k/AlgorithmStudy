input = "abcba"


def is_palindrome(string): #소주만병만주소
    if string[0]!=string[-1]:
        return False
    if len(string)<=1:
        return True
    return is_palindrome(string[1:-1]) #주만병만주


print(is_palindrome(input))