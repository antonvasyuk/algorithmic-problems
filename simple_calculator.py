def calculator(s):
    stack = []
    num = 0
    op = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack[-1] *= num
            elif op == '/':
                stack[-1] /= num
            num = 0
            op = s[i]
    return sum(stack)
