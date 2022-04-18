from collections import deque

deq1 = deque()
deq2 = deque()

n = int(input())

for i in range(n):
    action = input().split()

    if action[0] == '+':
        deq1.append(action[1])

    elif action[0] == '-':
        print(deq2.popleft())

    else:
        deq1.appendleft(action[1])

    if len(deq1) > len(deq2):
        deq2.append(deq1.popleft())
