def transform_to_postfix(exp):
    addsub = ['+', '-']
    multdiv = ['*', '/']

    stack_term = []
    stack_op = []

    exp += '$'
    idx = 0
    sym = ''
    while idx < len(exp) or stack_op:
        if idx < len(exp):
            sym = exp[idx]
            idx += 1

        # print(sym)
        
        if sym in addsub + multdiv + [')', '$']:
            while len(stack_term) >= 2 and stack_op and stack_op[-1] != '('\
                and (stack_op[-1] in multdiv or sym in addsub\
                or sym == ')' or sym == '$'):
                b = stack_term.pop()
                a = stack_term.pop()
                op = stack_op.pop()
                stack_term.append(f'{a}{b}{op}')

        if stack_op and sym == ')' and stack_op[-1] == '(':
            stack_op.pop()
        elif sym in addsub + multdiv + ['(']:
            stack_op.append(sym)
        else:
            stack_term.append(sym)
        
        # print(stack_term)
        # print(stack_op)
        # print("---------")
    
    return stack_term[0]

exp = input()
print(transform_to_postfix(exp))