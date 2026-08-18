"""
Problem Statement: Given the head of a linked list that may contain a cycle, return the starting point of that cycle. If there is no cycle in the linked list return null.
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
# node5.next = node3

head_node = node1

# approach 1 using dict with time cmpx is O(n) and space cmpx is O(n)

def first_approach(head_node):
    temp_dict = dict()

    temp_node = head_node
    starting_point = -1
    while temp_node != None:
        temp_dict[temp_node] = temp_dict.get(temp_node,0)+1

        if temp_dict.get(temp_node)==2:
            starting_point = temp_node.data
            return starting_point
        temp_node = temp_node.next
    return starting_point

print("1st approach : ", first_approach(head_node))

# approach 2 using  Floyd’s Cycle-Finding Algorithm

def second_approach(head_node):
    slow = head_node
    fast = head_node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            slow = head_node
            while slow != fast:
                slow = slow.next
                fast = fast.next
            if slow == fast:
                return slow.data
    return -1

print("2nd approach : ", second_approach(head_node))