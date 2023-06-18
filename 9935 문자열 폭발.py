# from datetime import datetime

def string_explode(s, bomb):
    stack = []
    bomb = list(bomb)
    for i in range(len(s)):
        stack.append(s[i])
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()
    res = ''.join(stack)
    return (res, "FRULA")[res == '']

# start = datetime.now()
s = input()
bomb = input()
print(string_explode(s, bomb))
# print(datetime.now() - start)
