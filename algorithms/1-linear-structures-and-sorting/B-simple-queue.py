class Queue:
    def __init__(self):
        self.q = []

    def push(self, n):
        print("ok")
        self.q.append(n)

    def pop(self):
        return self.q.pop(0)

    def front(self):
        return self.q[0]

    def size(self):
        return len(self.q)

    def clear(self):
        print("ok")
        self.q.clear()


que = Queue()

while True:
    action = input().split()

    if action[0] == "push":
        que.push(action[1])

    elif action[0] == "pop":
        a = que.pop()
        print(a)

    elif action[0] == "front":
        print(que.front())

    elif action[0] == "size":
        print(que.size())

    elif action[0] == "clear":
        que.clear()

    elif action[0] == "exit":
        print("bye")
        exit()
