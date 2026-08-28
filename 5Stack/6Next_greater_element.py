"""

Next Greater Element Using Stack


7

Problem Statement: Given an integer array A, return the next greater element for every element in A. The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. If it doesn't exist, return -1 for this element.

Examples
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.
Input : arr = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation : In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on the right and hence -1.

"""


# 1st approach

def first_approach(arr):
    result = []
    n = len(arr)

    for i in range(n):
        element = -1
        for j in range(i+1, n):
            if arr[j]>arr[i]:
                element = arr[j]
                break
        result.append(element)

    return result

arr = [1, 3, 2, 4]
print("1st approach : ", first_approach(arr))

# Before heading towards the second apporach read regarding the MONOTONIC STACK
# https://www.geeksforgeeks.org/dsa/introduction-to-monotonic-stack-2/


def second_approach(arr):
    n = len(arr)
    result = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        current_element = arr[i]
        while stack and stack[-1]<=current_element:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(current_element)

    return result

print("2nd approach ", second_approach(arr))
