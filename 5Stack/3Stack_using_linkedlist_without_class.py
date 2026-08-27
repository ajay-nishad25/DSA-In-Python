"""
Implement stack using linked list

Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a singly linked list. The implemented stack should support the following operations: push, pop, top, and isEmpty.

Implement the LinkedListStack class:

void push(int x): Pushes element x onto the stack.
int pop(): Removes and returns the top element of the stack.
int top(): Returns the top element of the stack without removing it.
boolean isEmpty(): Returns true if the stack is empty, false otherwise.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


head = None
tail = None # tail will act like index

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1
tail = node3

def push(data,tail):
    new_node = Node(data)
    tail.next = new_node
    tail = new_node
    return new_node


def pop(head,tail):
    if tail == None:
        print("Stack is already empty")
        return

    # if stack has single item 
    if head == tail:
        popped_data = tail.data
        head = None
        tail = None
        return popped_data,head,tail

    temp_node = head #2nd last node
    while temp_node.next != tail:
        temp_node = temp_node.next

    popped_data = tail.data
    temp_node.next = None
    tail = temp_node
    return popped_data,head,tail

def top(tail):
    if tail == None:
        print("Stack is empty")
        return

    return tail.data

def is_empty(tail):
    return  tail == None



def print_linked_list(head_node):
    temp_node = head_node
    while temp_node:
        print(temp_node.data, end=" => ")
        temp_node = temp_node.next
    print("null ")

print("Stack before operation : ")
print_linked_list(head)


print("Stack after push(4) : ")
tail = push(4,tail)
print_linked_list(head)


print("Stack after pop() : ")
popped_val, head, tail = pop(head, tail)
print("Popped value:", popped_val)
print_linked_list(head)

print("is stack is empty : ", is_empty(tail))


popped_val, head, tail = pop(head, tail)
popped_val, head, tail = pop(head, tail)
print_linked_list(head)

print("Top of stack is : ", top(tail))


popped_val, head, tail = pop(head, tail)
print("Top of stack is : ", top(tail))


print("is stack is empty : ", is_empty(tail))
