# https://www.codewars.com/kata/52774a314c2333f0a7000688


def valid_parentheses(string):
    openCount = 0
    for c in string:
        if c == '(':
            openCount += 1
        if c == ')':
            openCount -= 1
        if openCount < 0:
            return False
    return True if openCount == 0 else False


print(valid_parentheses("  (") == False)
print(valid_parentheses(")test") == False)
print(valid_parentheses("") == True)
print(valid_parentheses("hi())(") == False)
print(valid_parentheses("hi(hi)()") == True)
print(valid_parentheses('zed)(gjjetkvmvhmolk)cg') == False)
