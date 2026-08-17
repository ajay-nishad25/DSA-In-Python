"""
Problem Statement: Given the head of a singly linked list, 
write a program to reverse the linked list, and return the head pointer to the reversed list.
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

print("original linkedlist : ")
print_linked_list(head_node)


# approach 1 using other data structure like list bruteforce approach

def first_approach(head_node):
    temp_list = []
    temp_node = head_node

    if head_node is None:
        return None

    # traverse the LL and store node data into temp_list
    while temp_node is not None:
        temp_list.append(temp_node.data)
        temp_node = temp_node.next

    temp_list.reverse()
    temp_node = head_node
    index = 0

    while temp_node is not None:
        temp_node.data = temp_list[index]
        index+=1
        temp_node = temp_node.next    
    return head_node

print("1st approach to reverse LL : ")
head_node = first_approach(head_node)
print_linked_list(head_node)


# approach 1 using the other data structure like stack although this is also an bruteforce approach

def first_approach_v2(head_node):
    stack=[]
    if head_node is None:
        return None

    temp_node = head_node

    while temp_node:
        stack.append(temp_node.data)
        temp_node = temp_node.next

    temp_node = head_node
    while len(stack) != 0:
        temp_node.data = stack.pop()
        temp_node = temp_node.next
    return head_node

print("1st approach v2 to reverse LL : ")
head_node = first_approach_v2(head_node)
print_linked_list(head_node)

# approach 2 optimal approach using prev and curr node

def second_approach(head_node):
    if head_node == None:
        return None

    prev = None
    curr = head_node

    while curr != None:
        store_node = curr.next
        curr.next = prev
        prev = curr
        curr = store_node
    return prev

print("2nd approach to reverse LL : ")
head_node = second_approach(head_node)
print_linked_list(head_node)