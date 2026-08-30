"""
Implement Queue Using Array


5

Problem Statement: Implement a First-In-First-Out (FIFO) queue using an array. 
The implemented queue should support the following operations: push, dequeue, pop, and isEmpty.

Implement the ArrayQueue class:

void push(int x): Adds element x to the end of the queue.
int pop(): Removes and returns the front element of the queue.
int peek(): Returns the front element of the queue without removing it.
boolean isEmpty(): Returns true if the queue is empty, false otherwise.

"""

class Queue:

    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        self.rear = 0

    def is_empty(self):
        return self.rear == 0

    def push(self,data):

        if self.rear >= self.size:
            print("Queue is full")
            return
        
        self.queue[self.rear] = data
        self.rear += 1

    def pop(self):
        if self.is_empty():
            print("Queue is already empty")
            return

        self.queue[0] == None

        popped_data = self.queue[0]

        # since 0th element is removed now move every element towards left by 1 shift

        for i in range(1,self.rear):
            self.queue[i-1] = self.queue[i]

        self.queue[self.rear-1] = None
        self.rear -=1

        return popped_data

    def dispaly(self):
        print("Queue contains : ",self.queue)






queue = Queue(4)
queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.dispaly()

queue.push(40)

queue.dispaly()

queue.pop()

queue.dispaly()

queue.pop()

queue.pop()

queue.dispaly()

queue.pop()
queue.dispaly()
queue.pop()



