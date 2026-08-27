
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        if self.is_empty(): #initial stack element
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.head.data

    def dispaly(self):
        temp_node = self.head

        while temp_node:
            print(temp_node.data, end=" => ")
            temp_node = temp_node.next

        print(" null")


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.dispaly()

stack.pop()
stack.dispaly()
stack.pop()

stack.dispaly()

print("peek element in stack : ",stack.peek())

print("is stack empty : ", stack.is_empty())

stack.push(40)
stack.dispaly()