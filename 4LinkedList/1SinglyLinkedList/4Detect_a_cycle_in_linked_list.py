"""
Problem Statement: Given a Linked List, determine whether the linked list contains a cycle or not.

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# cycle node
node5.next = node3

head_node = node1

def print_linked_list(head_node):
    temp_node = head_node
    while temp_node:
        print(temp_node.data, end=" => ")
        temp_node = temp_node.next
    print("null ")



# approach 1 bruteforce approach using hashmap i.e dict

def first_approach(head_node):
    hasmap = dict()

    temp_node = head_node
    while temp_node!=None:
        if hasmap.get(temp_node.data):
            return True
        else:
            hasmap[temp_node.data] = 1
        temp_node = temp_node.next
    return False

print("1st approach using hashmap : ", first_approach(head_node))

# approach 2 optimal approach

def second_approach(head_node):
    slow = head_node
    fast = head_node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print("2nd approach using slow and fast method : ", second_approach(head_node))