"""
Next Smaller Element

Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
If there is no smaller element to the right, then the NSE is -1.

Examples
Example 1:
Input:
arr = [4, 8, 5, 2, 25]
Output:
[2, 5, 2, -1, -1]
Explanation:

- For 4, the next smaller element is 2.
- For 8, the next smaller element is 5.
- For 5, the next smaller element is 2.
- For 2, there is no smaller element to its right → -1.
- For 25, no smaller element exists → -1.

Example 2:
Input:
arr = [10, 9, 8, 7]
Output:
[9, 8, 7, -1]
Explanation:

Each element’s next right neighbor is smaller.
Each element’s next right neighbor is smaller.

"""

# first approach i.e brute force approach time cmpx O(n^2) and space O(n)

arr = [4, 8, 5, 2, 25]


def first_approach(arr):
    n = len(arr)
    
    result = [-1]*n
    
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
    
    return result

print("1st approach : ", first_approach(arr))


def second_approach(arr):
    n = len(arr)
    
    result = [-1]*n
    stack = []
    
    for i in range(n-1, -1, -1):
        
        while stack and arr[i]<=stack[-1]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

print("2nd approach : ", second_approach(arr))