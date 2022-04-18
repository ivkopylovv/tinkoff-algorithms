def solve(a, b, sign):
    if (sign == '+'):
        return a + b

    elif (sign == "-"):
        return a - b

    elif (sign == "*"):
        return a * b

    else:
        return 0


stack = []
postfixstr = input().split()

for i in range(len(postfixstr)):
    if postfixstr[i].isdigit():
        stack.append(int(postfixstr[i]))

    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(solve(a, b, postfixstr[i]))

print(stack.pop())
