class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# generic and easy way of implemetation of DLL with manual link connection
# # Create nodes
# node1 = Node(5)
# node2 = Node(6)
# node3 = Node(7)
# node4 = Node(8)
# node5 = Node(9)

# # Forward links (next)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Backward links (prev)
# node2.prev = node1
# node3.prev = node2
# node4.prev = node3
# node5.prev = node4


head_node = None
tail_node = None


user_input = list(map(int,input("Enter numbers : ").split()))

for num in user_input:
    new_node = Node(num)
    if head_node == None:
        head_node = new_node
        tail_node = new_node
    else:
        tail_node.next = new_node
        new_node.prev = tail_node
        tail_node = new_node

# generic methods

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

def get_length(head_node):
    if head_node == None:
        return 0

    temp_node = head_node
    index = 0
    while temp_node:
        index +=1
        temp_node = temp_node.next
    return index

print("forward print : ")
print_forward(head_node)
print("backward print : ")
print_backward(tail_node)


# operations method

def insert_at_position(head_node,data,k):
    n = get_length(head_node)
    if n==0 or k>n:
        return head_node
    temp_node = head_node
    if k == 1:
        new_node = Node(data)
        new_node.next = head_node
        head_node.prev = new_node
        return new_node

    while k>2 and temp_node:
        k-=1
        temp_node = temp_node.next

    if temp_node:
        new_node = Node(data)
        store = temp_node.next
        temp_node.next = new_node
        new_node.prev = temp_node
        new_node.next = store
        if store:
            store.prev = new_node
    return head_node

print("insert at position : ")
head_node = insert_at_position(head_node,2,2)
print_forward(head_node)