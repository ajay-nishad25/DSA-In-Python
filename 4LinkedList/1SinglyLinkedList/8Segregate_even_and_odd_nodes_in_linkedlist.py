"""
Problem Statement: Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list. 
Consider the 1st node to have index 1 and so on. 
The relative order of the elements inside the odd and even group must remain the same as the given input.

Input: 1→2→3→4→5→6→Null
Output: 2→4→6→1→3→5→Null
Explanation : Odd Nodes in LinkedList are 1,3,5 and Even Nodes in LinkedList are 2,4,6
In Modified LinkedList all even Nodes comes before all Odd Nodes. So Modified LinkedList looks like 2→4→6→1→3→5→Null. Order of even and odd Nodes is 
maintained in modified LinkedList.

Input: 1→3→5→Null
Output: 1→3→5→Null
Explanation: As there are no Even Nodes in LinkedList, The Modified LinkedList is same as Original LinkedList.
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



# approach 1 using array 
# time cmpx is O(n) for length
# O(n) for even number
# O(n) for odd number
# O(n) for constructing new linkedlist
# so overall time cmpx is O(n)
# space cmpx is O(n) for array list


def first_approach(head_node):
    # first get the length of linkedlist
    n = get_length(head_node)
    if n == 0 or n == 1:
        return head_node

    # now create same size array 
    result_list = [0]*n
    index = 0
    temp_node = head_node

    # now traverse list to find the even number and store initially
    while temp_node:
        if temp_node.data % 2 == 0: #even
            result_list[index] = temp_node.data
            index +=1
        temp_node = temp_node.next

    temp_node = head_node

    while temp_node:
        if temp_node.data % 2 != 0: #odd
            result_list[index] = temp_node.data
            index +=1
        temp_node = temp_node.next

    # now since we have the result in result_list for even and odd element of linkedlist by order
    # now we can construct new linkedlist using the result_list
    new_linkedlist_head = None
    new_linkedlist_tail = None
    for num in result_list:
        new_node = Node(num)
        if new_linkedlist_head == None:
            new_linkedlist_head = new_node
            new_linkedlist_tail = new_node
        else:
            new_linkedlist_tail.next = new_node
            new_linkedlist_tail = new_node
    return new_linkedlist_head



new_linkedlist_head = first_approach(head_node)
print("1st approach : ")
print_linked_list(new_linkedlist_head)

# approach 2  time cmpx is o(N) and space cmpx O(n)

def second_approach(head_node):

    even_head = even_tail = None
    odd_head = odd_tail = None
    temp_node = head_node
    while temp_node:
        data = temp_node.data
        new_node = Node(data)

        if data % 2 == 0: #even number
            if even_head == None:
                even_head = new_node
                even_tail = new_node
            else:
                even_tail.next = new_node
                even_tail = new_node
        else:
            if odd_head == None: #odd number
                odd_head = new_node
                odd_tail = new_node
            else:
                odd_tail.next = new_node
                odd_tail = new_node

        temp_node = temp_node.next

    even_tail.next = odd_head
    return even_head

new_linkedlist_head = second_approach(head_node)
print("2nd approach : ")
print_linked_list(new_linkedlist_head)