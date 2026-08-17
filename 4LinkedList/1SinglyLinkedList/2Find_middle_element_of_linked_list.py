"""
Problem Statement: Given the head of a linked list of integers, 
determine the middle node of the linked list. 
However, if the linked list has an even number of nodes, return the second middle node.

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


# approach 1 bruteforce approach 
"""
find the length of linked list and traverse till that n//2 and if lenght is even then n+1//2
"""

def get_length(head_node):
    temp_node = head_node
    index = 0

    if head_node is None:
        return index

    while temp_node!=None:
        index+=1
        temp_node = temp_node.next

    return index

def first_approach(head_node):
    n = get_length(head_node)

    if head_node == None or n ==0:
        return -1

    temp_node = head_node
    length = -1

    if n%2 == 0: #even length
        length = (n+1)//2
    else:
        length = n//2

    while length != 0:
        temp_node = temp_node.next
        length -=1
    return temp_node.data


print("length of linkedlist is : ", get_length(head_node))
print("Middle element of linkedlist is : ", first_approach(head_node))


# approach 2 [hare and tortoise approach]

def second_approach(head_node):
    if head_node is None:
        return -1
    slow = head_node
    fast = head_node

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next

    return slow.data
print("Approach 2 Middle element of linkedlist is : ", second_approach(head_node))

