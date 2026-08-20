class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

headnode = None
tailnode = None


userinput = input("Enter numbers : ")

print(userinput)
templist = []

for i in userinput.split():
    if i.isdigit():
        templist.append(int(i))

userinput = templist

for num in userinput:
    newnode = Node(num)
    if headnode == None:
        headnode = newnode
        tailnode = newnode
    else:
        tailnode.next = newnode
        newnode.prev = tailnode
        tailnode = newnode

# generic methods

def print_forward(headnode):
    tempnode = headnode
    while tempnode:
        print(tempnode.data, end=" <=> ")
        tempnode = tempnode.next
    print("null")

def get_length(headnode):
    if headnode == None:
        return 0

    tempnode = headnode
    index = 0
    while tempnode:
        index +=1
        tempnode = tempnode.next
    return index

print("Doubly linkedlist : ")
print_forward(headnode)

# approach 1 using array list

def first_approach(headnode):
    if headnode == None:
        return headnode

    templist = []
    tempnode = headnode

    while tempnode:
        templist.append(tempnode.data)
        tempnode = tempnode.next

    tempnode = headnode
    while tempnode:
        data = templist.pop()
        tempnode.data = data
        tempnode = tempnode.next
    return headnode

    

print("1st apporach : ")
headnode = first_approach(headnode)
print_forward(headnode)


# approach 2nd 

def second_approach(headnode):
    if headnode == None:
        return headnode
    
    currnode = headnode
    prevnode = None
    while currnode:
        storenode = currnode.next
        currnode.next = prevnode
        prevnode = currnode
        currnode = storenode

    return prevnode

print("2nd apporach : ")
headnode = second_approach(headnode)
print_forward(headnode)


