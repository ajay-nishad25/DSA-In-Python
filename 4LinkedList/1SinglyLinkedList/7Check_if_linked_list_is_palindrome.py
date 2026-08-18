"""
Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list. If there's no loop present, return 0.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

user_input = list(map(int,input("Enter numbers : ").split()))

head_node = None
tail_node = None

for num in user_input:
    new_node = Node(num)

    if head_node == None: #first node
        head_node = new_node
        tail_node = new_node
    else:
        tail_node.next = new_node
        tail_node = new_node



def print_linked_list(head_node):
    temp_node = head_node
    while temp_node:
        print(temp_node.data, end=" => ")
        temp_node = temp_node.next
    print("null ")


print_linked_list(head_node)

# apporach 1 using stack with time cmpx O(n) and space O(n)

def first_approach(head_node):
    stack = []

    temp_node = head_node
    while temp_node:
        stack.append(temp_node.data)
        temp_node = temp_node.next

    temp_node = head_node

    while temp_node:
        if temp_node.data != stack[-1]:
            return False
        stack.pop()
        temp_node = temp_node.next
    return True

print("1st approach : ", first_approach(head_node))

# approach 2 optimal using rabbit and tortoise approach with time O(n) and space O(1)

def second_approach(head_node):
    fast =head_node
    slow = head_node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next


    # reverse list form slow to end
    prev = None
    curr = slow

    while curr:
        store = curr.next
        curr.next = prev
        prev = curr
        curr = store

    # now prev holds the reversed list starting point

    first_half = head_node
    second_half = prev

    while second_half and first_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

print("2nd approach ",second_approach(head_node))

