"""
Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list. If there's no loop present, return 0.
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

# approach 1 using hasmap witht time cpmx O(n) and space cmpx O(n)

def first_approach(head_node):
    temp = dict()
    temp_node = head_node
    index = 1
    while temp_node != None:
        if temp_node in temp:
            return index-temp.get(temp_node)
        temp[temp_node] = index
        temp_node = temp_node.next
        index +=1
    return -1

print("1st approach ", first_approach(head_node))


# approach 2 optimal approach with time O(n) and space cmpx O(1)

def second_approach(head_node):

    fast = head_node
    slow = head_node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            index = 1
            slow = slow.next
            while slow!=fast:
                index +=1
                slow = slow.next
            return index
    return 0 

print("2nd approach : ", second_approach(head_node))