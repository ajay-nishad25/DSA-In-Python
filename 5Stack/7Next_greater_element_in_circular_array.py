"""

Next Greater Element - 2

Problem Statement: Given a circular integer array arr, return the next greater element for every element in arr.
The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.
If it doesn't exist, return -1 for that element element.

Examples
Example 1:
Input:
arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
Output:
[10, -1, 6, 6, 2, 6, 7, 7, 9, 9, 10]
Explanation:
For the first element in arr i.e, 3, the greater element which comes next to it while traversing and is closest to it is 10. Hence,10 is present on index 0 in the resultant array. 
Now for the second element i.e, 10, there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.

Example 2:
Input:
arr = [5, 7, 1, 7, 6, 0]
Output:
[7, -1, 7, -1, 7, 5]
Explanation:
For the first element in arr i.e, 5, the greater element which comes next to it while traversing and is closest to it is 7. Now for the second element i.e, 7, 
there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.
"""


# first approach using 2 loop with time cmpx is O(n^2) and space O(n)

arr = [5, 7, 1, 7, 6, 0]
n = len(arr)

def first_approach(arr,n):
    result = [-1]*n

    for i in range(n):

        # forward loop
        found = False
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                found = True
                break 
        
        if not found : # since we didnt found the element start checking from 0th index
            for k in range(0,i+1):
                if arr[k] > arr[i]:
                    result[i] = arr[k]
                    break

    return result

print("1st approach : ", first_approach(arr,n))


# second approach using monotonic stack with the cmpx O(n*2) and space cmpx for result is O(n) and O(n) for stack in worst case

def second_approach(arr,n):
    result = [-1]*n
    nums1 = arr
    nums2 = arr
    temp = nums1 + nums2

    stack = []

    for i in range(2*n-1, -1, -1):
        current = temp[i]
        while stack and current >= stack[-1]:
            stack.pop()
            
        if i<n and stack:
            result[i] = stack[-1]
            
        stack.append(current)

    return result


print("2nd approach : ", second_approach(arr,n))