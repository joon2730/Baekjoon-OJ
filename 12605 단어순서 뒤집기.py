def flip_words(s):
    lst = s.split()
    res = []
    while lst:
        res.append(lst.pop())
    return res

n = int(input())
for i in range(n):
    s = input()
    print(f'Case #{i+1}: ', end='')
    print(*flip_words(s))