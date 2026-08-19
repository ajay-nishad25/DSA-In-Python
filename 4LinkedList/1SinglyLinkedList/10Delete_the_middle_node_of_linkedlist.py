"""
Problem Statement: Given the head of a linked list of integers, delete the middle node of the linked list and return the modified head. However, if the linked list has an even number of nodes, delete the second middle node.
"""

"""
Input: 1->2->3->4->5 

Output: 1->2->4->5

Explanation: Node with value 3 is at the middle node and deleted.

Input: 1->2->3->4

Output: 1->2->4

Explanation: The linked list has an even number of nodes hence we delete the second middle node which is 3.
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


# approach 1 
# time cmpx is O(n) for length
# again travesing till O(n//2)

def first_apporach(head_node):

    if head_node is None or head_node.next is None:
        return None

    n = get_length(head_node)

    element_index = n//2
    index = 1
    cur = head_node
    while element_index != index:
        index+=1
        cur = cur.next

    cur.next = cur.next.next
    return head_node

head_node = first_apporach(head_node)
print("1st approach : ")
print_linked_list(head_node)

# approach 2

def second_approach(head_node):
    
    if head_node is None or head_node.next is None:
        return None
    
    slow = head_node
    fast = head_node.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = slow.next.next
    return head_node

head_node = second_approach(head_node)
print("2nd apporach : ")
print_linked_list(head_node)
