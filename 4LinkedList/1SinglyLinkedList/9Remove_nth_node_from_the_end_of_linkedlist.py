"""
Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.
"""

"""
Input:  5->1->2, N=2
Output: 5->2
Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.

Input:  1->2->3->4->5, N=3
Output: 1->2->4->5
Explanation: The 3rd node from the end is 3, therefore, we remove 3 from the linked list.
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

nth = int(input("Enter Nth node from end : "))

# generic functions

def print_linked_list(head_node):
    temp_node = head_node
    while temp_node:
        print(temp_node.data, end=" => ")
        temp_node = temp_node.next
    print("null ")

def get_length(head_node):
    temp_node = head_node
    index = 0
    while temp_node:
        index += 1
        temp_node = temp_node.next
    return index

print_linked_list(head_node)

# approach 1 
# time cpmx
# O(n) for length
# O(n-nth+1) for traversing till the last Nth node
# space cmpx is O(1)


def first_approach(head_node,n):
    length = get_length(head_node)
    if n == length:
        return head_node.next

    element_index = (length-n)+1
    current = head_node
    prev = None
    index = 1
    while element_index != index:
        prev = current
        current = current.next
        index +=1

    prev.next = current.next
    current.next = None
    return head_node

print("1st approach : ")
head_node = first_approach(head_node,nth)
print_linked_list(head_node)


# approach 2
# time cmpx is O(n)
# space cmpx is O(1)

def second_approach(head_node, n):
    # temp dummy node
    new_node = Node(0)
    new_node.next = head_node

    dummy_node = new_node

    fast = slow = dummy_node
    
    for i in range(n+1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy_node.next

print("2nd approach : ")
head_node = second_approach(head_node,nth)
print_linked_list(head_node)