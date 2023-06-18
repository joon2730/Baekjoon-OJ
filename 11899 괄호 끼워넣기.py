def count_num_bracket_to_insert(s):
    num = 0
    cnt_open_braket = 0
    for c in s:
        if c == '(':
            cnt_open_braket += 1
        elif c == ')':
            if cnt_open_braket <= 0:
                num += 1
            else:
                cnt_open_braket -= 1
    num += cnt_open_braket
    return num

s = input()
print(count_num_bracket_to_insert(s))