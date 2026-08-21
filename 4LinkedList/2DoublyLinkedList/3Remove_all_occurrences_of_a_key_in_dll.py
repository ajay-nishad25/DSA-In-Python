"""
Delete all occurrences of a key in DLL


0

Problem Statement: Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target and return the head of the modified linked list.

Examples
Input: head -> 1 <-> 2 <-> 3 <-> 1 <-> 4, target = 1

Output: head -> 2 <-> 3 <-> 4
Input: head -> 2 <-> 3 <-> -1 <-> 4 <-> 2, target = 2

Output: head -> 3 <-> -1 <-> 4

"""

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

headnode = None
tailnode = None


userinput = input("Enter numbers : ")

print(userinput)
templist = []

for i in userinput.split():
    if i.isdigit():
        templist.append(int(i))

userinput = templist

for num in userinput:
    newnode = Node(num)
    if headnode == None:
        headnode = newnode
        tailnode = newnode
    else:
        tailnode.next = newnode
        newnode.prev = tailnode
        tailnode = newnode

# generic methods

def print_forward(headnode):
    tempnode = headnode
    while tempnode:
        print(tempnode.data, end=" <=> ")
        tempnode = tempnode.next
    print("null")

def get_length(headnode):
    if headnode == None:
        return 0

    tempnode = headnode
    index = 0
    while tempnode:
        index +=1
        tempnode = tempnode.next
    return index

print("Doubly linkedlist : ")
print_forward(headnode)


# approach 1 using array 
# time cmpx is O(n) for storing element into list
# O(n) for creating new DLL 

def first_approach(headnode, target):
    if headnode == None:
        return headnode

    templist = []
    tempnode = headnode
    while tempnode:
        if tempnode.data != target:
            templist.append(tempnode.data)
        tempnode = tempnode.next

    print(templist)
    # now create new DLL
    if len(templist) == 0:
        return headnode

    head = None
    tail = None

    for num in templist:
        newnode = Node(num)
        if head == None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            newnode.prev = tail
            tail = newnode
    return head

print("1st approach : ")
headnode = first_approach(headnode, 1)
print_forward(headnode)


def second_approach(headnode, target):
    if headnode == None:
        return headnode

    head = None
    current = headnode

    while current:

        if head is None and current.data != target:
            head = current

        if current.data == target:
            prevnode = current.prev
            nextnode = current.next

            if prevnode:
                prevnode.next = nextnode
            if nextnode:
                nextnode.prev = prevnode

            # disconnect current node
            current.next = None
            current.prev = None
            current = nextnode
        else:
            current = current.next
    print_forward(head)
    print(head.prev)
    print(head.next)

second_approach(headnode,1)