from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self,val):
        self.queue.appendleft(val)
        return True
    def dequeue(self):
        return self.queue.pop()
    def size(self):
        return self.queue[2]
q1 = Queue()
q1.push(5)
q1.push(4)
q1.push(3)
q1.push(2)
q1.push(1)

print(q1.size())