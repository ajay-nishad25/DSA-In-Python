"""
Implement Min Stack : O(2N) and O(N) Space Complexity

Problem Statement: Design a stack that supports the following operations in constant time: push, pop, top, and retrieving the minimum element.

Implement the MinStack class:

MinStack(): Initializes the stack object.
void push(int val): Pushes the element val onto the stack.
void pop(): removes the element on the top of the stack.
int top(): gets the top element of the stack.
int getMin(): retrieves the minimum element in the stack.

Examples
Example 1:
Input:
 ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]  
[ [], [-2], [0], [-3], [ ], [ ], [ ], [ ] ]  
Output:
 [null, null, null, null, -3, null, 0, -2]  
Explanation:
  
MinStack minStack = new MinStack();  
- minStack.push(-2);  
- minStack.push(0);  
- minStack.push(-3);  
- minStack.getMin(); // returns -3  
- minStack.pop();  
- minStack.top(); // returns 0  
- minStack.getMin(); // returns -2  

Example 2:
Input:
 ["MinStack", "push", "push", "getMin", "push", "pop", "getMin", "top"]  
[ [ ], [5], [1], [ ], [3], [ ], [ ], [ ] ]  
Output:
 [null, null, null, 1, null, null, 1, 1]  
Explanation:
  
MinStack minStack = new MinStack();  
- minStack.push(5);  
- minStack.push(1);  
- minStack.getMin(); // returns 1  
- minStack.push(3);  
- minStack.pop();  
- minStack.getMin(); // returns 1  
- minStack.top(); // returns 1
"""


# 1st approach time O(1) for push, pop, top, get_min and space cmpx is O(2N)
# why O(2N) 
"""

Visual Example:
If you push 3 elements: push(5), push(2), push(8):

Standard Stack (N elements):
[ 5, 2, 8 ] -> 3 integers stored.

Min Stack with Pairs (2N elements):
[ (5, 5), (2, 2), (8, 2) ] -> 6 integers stored (2 * 3).

For an input size of N items, the stack holds 2 * N values in memory:

N actual data values

N minimum-tracking values

Big-O Notation vs. Exact Space:

Asymptotic Complexity:
In standard Big-O notation, constant factors are dropped:
O(2N) -> O(N)

Why interviewers specify O(2N):
They use the term O(2N) to explicitly highlight the 2x memory overhead compared to an algorithm that stores only 1N integers.

"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self,value):
        if not self.stack: #initial element
            data = {
                "cur": value,
                "min": value
            }
            self.stack.append(data)
        else:
            # peek the previoud element
            peeked_element = self.stack[-1]
            data = {
                "cur":value,
                "min": min(peeked_element["min"],value)
            }
            self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty ")
            return
        else:
            data = self.stack.pop()
            return data['cur']

    def top(self):
        if len(self.stack) == 0:
            print("stack is empty ")
            return
        else:
            data = self.stack[-1]
            return data["cur"]

    def get_min(self):
        if len(self.stack) == 0:
            print("stack is empty ")
            return
        else:
            data = self.stack[-1]
            return data['min']

    def dispaly(self):
        for element in self.stack:
            print(element, end=" ")
        print()


stack = MinStack()

stack.push(7)
stack.push(8)
stack.push(6)
stack.push(4)
stack.push(9)
stack.push(10)
stack.push(12)

stack.dispaly()

print("min in stack is : ", stack.get_min())
print("top in stack is : ",stack.top())

print("popped element in stack is : " ,stack.pop())
stack.dispaly()



# approach 2 using 2 stack with time O(1) for all operations but space is O(n+n) i.e O(2n)


print("==================== Second approach ==================================")

class MinStack2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self,value):
        self.stack1.append(value)
        if not self.stack2: #initial stack2 is empty
            self.stack2.append(value)
            return
        self.stack2.append(min(self.stack1[-1],self.stack2[-1]))


    def pop(self):
        data = self.stack1.pop()
        self.stack2.pop()
        return data

    def top(self):
        return self.stack1[-1]

    def get_min(self):
        return self.stack2[-1]

    def dispaly(self):
        for element in self.stack1:
            print(element, end=" ")
        print()


stack = MinStack2()

stack.push(7)
stack.push(8)
stack.push(6)
stack.push(4)
stack.push(9)
stack.push(10)
stack.push(12)

stack.dispaly()

print("min in stack is : ", stack.get_min())
print("top in stack is : ",stack.top())

print("popped element in stack is : " ,stack.pop())
stack.dispaly()
print("min in stack is : ", stack.get_min())

stack.pop()
stack.pop()
stack.pop()
stack.dispaly()
print("min in stack is : ", stack.get_min())
