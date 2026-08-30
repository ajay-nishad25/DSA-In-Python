"""
Implement Queue using Linked List

Problem Statement: Implement a First-In-First-Out (FIFO) queue using a singly linked list. The implemented queue should support the following operations: push, pop, peek, and isEmpty.

Implement the LinkedListQueue class:

void push(int x): Adds element x to the end of the queue.
int pop(): Removes and returns the front element of the queue.
int peek(): Returns the front element of the queue without removing it.
boolean isEmpty(): Returns true if the queue is empty, false otherwise.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class QueueLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def push(self,data):
        new_node = Node(data)

        if self.head == None: #initial element of LL
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            print("Queue is already empty")
            return

        if not self.head.next: # linked list has only single element
            data = self.head.data
            self.head = None
            return data

        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return 

        return self.head.data

    def display(self):

        if self.is_empty():
            print("Cant print since queue is empty")
            return

        
        temp_node = self.head
        while temp_node:
            print(temp_node.data , end=" ")
            temp_node = temp_node.next
        print()


queue = QueueLinkedlist()

queue.push(12)
queue.push(13)
queue.push(14)
queue.push(15)
queue.push(16)
queue.push(17)


queue.display()
queue.pop()
queue.pop()

queue.display()


queue.pop()

queue.pop()
queue.pop()


queue.display()
