stack = [0] * 10
index = 0

def push(data):
    global index
    if index >= len(stack):
        print("Stack Overflow")
        return
    stack[index] = data
    index += 1

def pop():
    global index
    if isEmpty():
        print("Stack Underflow")
        return None
    index -= 1             
    data = stack[index]
    stack[index] = 0
    return data

def top():
    if isEmpty():
        return None
    return stack[index - 1]  

def isEmpty():
    return index == 0

def size():
    return index

print("initial stack : ", stack)
push(10)
push(20)
push(23)
push(24)
push(25)
push(26)
push(27)
push(28)
push(29)
push(30)

topElement = top()
print("after push operation : ", stack)
print("top element :", topElement) 
print("popped element :", pop())      
print("stack after pop :", stack)