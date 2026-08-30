"""
Implement Stack using single Queue


Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a single queue. The implemented stack should support the following operations: push, pop, top, and isEmpty.

Implement the QueueStack class:

push(int x): Pushes element x onto the stack.
pop(): Removes and returns the top element of the stack.
top(): Returns the top element of the stack without removing it.
isEmpty(): Returns true if the stack is empty, false otherwise.

"""



from queue import Queue

class StackQueue:
    def __init__(self,size):
        self.size = size
        self.stackqueue = Queue(self.size)

    def is_empty(self):
        return self.stackqueue.empty()

    def is_full(self):
        return self.stackqueue.full()

    def push(self,data):
        if self.is_full():
            print("Stack is already full ")
            return

        self.stackqueue.put(data)
        current_size = self.stackqueue.qsize()

        for _ in range(current_size-1):
            self.stackqueue.put(self.stackqueue.get())

    def pop(self):
        if self.is_empty():
            print("Stack is already empty ")
            return
        data = self.stackqueue.get()
        return data

    def peek(self):
            if self.is_empty():
                print("Stack is empty")
                return None
            return self.stackqueue.queue[0]

    def dispaly(self):
        print(list(self.stackqueue.queue))

queue = StackQueue(5)

queue.push(23)
queue.push(4)
queue.push(3)
queue.push(2)

queue.dispaly()
queue.push(9)

queue.dispaly()

queue.push(10)

queue.pop()
queue.pop()
queue.pop()

queue.dispaly()

print("top of the stack is : ",queue.peek())

queue.pop()

queue.pop()

queue.pop()

print("top of the stack is : ",queue.peek())

