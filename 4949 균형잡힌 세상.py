# https://www.acmicpc.net/problem/4949

def is_pair(a, b):
        if a == "(" and b == ")":
            return True
        elif a == "{" and b == "}":
            return True
        elif a == "[" and b == "]":
            return True
        return False

def is_balanced(s):
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        elif c == ")" or c == "}" or c == "]": 
            if stack and is_pair(stack[-1], c):
                stack.pop()
            else:
                return False
    return not stack

while True:
    s = input()
    if s == '.':
        break
    res = ("no", "yes")[is_balanced(s)]
    print(res)
