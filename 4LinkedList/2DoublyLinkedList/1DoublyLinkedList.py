

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Create nodes
node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)
node5 = Node(9)

# Forward links (next)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Backward links (prev)
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

head_node = node1
tail_node = node5

def print_forward(head_node):
    temp_node = head_node
    print("null", end=" <=> ")
    while temp_node:
        print(temp_node.data, end=" <=> ")
        temp_node = temp_node.next

    print("null")

def print_backward(tail_node):
    temp_node = tail_node
    print("null", end=" <=> ")
    while temp_node:
        print(temp_node.data, end=" <=> ")
        temp_node = temp_node.prev

    print("null")


print_forward(head_node)
print_backward(tail_node)