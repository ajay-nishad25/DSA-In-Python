
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def print_linked_list(head_node):
    temp_node = head_node
    while temp_node:
        print(temp_node.data, end=" => ")
        temp_node = temp_node.next
    print("null ")


# example
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)

# n1.next = n2
# n2.next = n3
# n3.next = n4

# temp_node = n1

# while temp_node:
#     print(temp_node.data, end=" -> ")
#     temp_node = temp_node.next


# now take the user input 

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

print_linked_list(head_node)

# question 1 insert at the head of linkedlist 

def insert_at_head(head_node,data):
    if head_node is None: # linkedlist is not created yet now create
        new_node = Node(data)
        head_node = new_node
        return head_node

    else:
        new_node = Node(data)
        new_node.next = head_node
        head_node = new_node
        return head_node



head_node = insert_at_head(head_node,23)
print("Insert data at head of linked list")
print_linked_list(head_node)


# question 2 insert at the tail of linkedlist 

def insert_at_tail(tail_node,head_node,data):
    if tail_node == None and head_node == None: # linkedlist in not created yet create new node 
        head_node = insert_at_head(head_node,data)
        tail_node = head_node
        return tail_node
    else : 
        new_node = Node(data)
        tail_node.next = new_node
        tail_node = new_node
        return tail_node

tail_node = insert_at_tail(tail_node,head_node,6)
print("Insert data at tail of linked list")
print_linked_list(head_node)


# question 3 delete at the head of linkedlist 

def delete_at_head(head_node):
    # if head_node is None i.e linkedlist is not created yet
    if head_node is None:
        return None
    # if head_node only consist single element 
    if head_node.next == None:
        head_node = None
        return head_node
    else:
        head_node = head_node.next
        return head_node

print("Delete at head of linked list")
head_node = delete_at_head(head_node)
print_linked_list(head_node)

# question 4 delete at the tail of linkedlist

def delete_at_tail(tail_node,head_node):
    # if tail_node is none that means the linkedlist is not yet created so just return None
    if tail_node is None:
        return None
    else:
        # travers till the 2nd last node of list and move the tail pointer to 2nd last node
        temp_node = head_node
        while temp_node.next.next != None:
            temp_node = temp_node.next
        temp_node.next = None
        tail_node = temp_node
        return tail_node

tail_node = delete_at_tail(tail_node,head_node)
print("Delete at tail of linked list")
print_linked_list(head_node)

# question 5 delete by element of linkedlist

def delete_by_element(head_node, data):
    # Case 1: Empty list
    if head_node is None:
        return None

    # Case 2: Target is the first (head) node
    if head_node.data == data:
        return head_node.next

    # Case 3: Target is in the middle or at the end
    prev = None
    current = head_node

    while current.data != data and current != None:
        prev = current
        current = current.next

    if current != None:
        prev.next = current.next

    return head_node

print("Delete by element")
head_node = delete_by_element(head_node,3)
print_linked_list(head_node)

# question 6 delete by index of linkedlist

def delete_by_index(head_node,element_idx):
    if head_node == None or element_idx<0:
        return None
    
    if element_idx == 0: #delete the head_node
        return head_node.next
    
    prev = None
    current = head_node
    index = 0 

    while index!=element_idx and current != None:
        prev = current
        current = current.next
        index += 1

    if index == element_idx and current is not None:
        prev.next = current.next
    return head_node

print("Delete by index")
head_node = delete_by_index(head_node,1)
print_linked_list(head_node)


# question 7 update by element of linkedlist

def update_by_element(head_node,data,new_data):
    if head_node is None:
        return None

    if head_node.data == data:
        head_node.data = new_data
        return head_node

    current = head_node

    while current.data != data and current != None:
        current = current.next

    if current != None:
        current.data = new_data

    return head_node

print("Update by element")
head_node = update_by_element(head_node,4,5)
print_linked_list(head_node)

# question 8 update element by index of linkedlist

def udpate_by_index(head_node,element_idx,new_data):
    if head_node == None or element_idx<0:
        return None
    
    if element_idx == 0:
        head_node.data = new_data
        return head_node
    
    current = head_node
    index = 0 

    while index!=element_idx and current != None:
        current = current.next
        index += 1

    if index == element_idx and current is not None:
        current.data = new_data
    return head_node

print("Update by index")
head_node = udpate_by_index(head_node,2,7)
print_linked_list(head_node)

print("filled data for new operations")
tail_node = insert_at_tail(tail_node,head_node,34)
tail_node = insert_at_tail(tail_node,head_node,35)
tail_node = insert_at_tail(tail_node,head_node,36)
print_linked_list(head_node)

# question 9 find the length of linkedlist 

def length_of_list(head_node):
    if head_node is None:
        return 0
    else:
        index = 0 
        temp_node = head_node
        while temp_node != None:
            index +=1
            temp_node = temp_node.next
        return index

print("Length of linked list is : ", length_of_list(head_node))

# question 10 find the element in the linkedlist

def search_list(head_node,element):
    if head_node is None:
        return 0
    else:
        index = 0
        temp_node = head_node
        while temp_node != None and temp_node.data != element:
            index +=1
            temp_node = temp_node.next
        if temp_node != None:
            return index

print("Element at index : ",search_list(head_node,35))