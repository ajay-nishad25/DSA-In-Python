"""
Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Example 2:
Input: prices = {1, 0, 1, 1, 0, 1} 
Output: 2
Explanation: There are two consecutive 1's in the array. 
"""


# approach 1 time cmpx is O(n^2) and space is O(1)

arr = [1, 1, 0, 1, 1, 1]
n = len(arr)

def first_approach(arr,n):

    counter = 0

    for i in range(n):
        if arr[i] == 0:
            continue
        inner_counter = 1
        for j in range(i+1,n):
            if arr[i]==1 and arr[j]==1:
                inner_counter +=1
            else :
                break
        counter = max(counter,inner_counter)
        

    return counter

print("1st approach : ", first_approach(arr,n))

# approach 2 time cmpx is O(n) and space cmpx is O(1)
arr = [0, 1, 1, 0]
n = len(arr)

def second_approach(arr,n):
    count = 0
    temp_counter = 0

    for i in range(n):
        if arr[i] == 1:
            temp_counter +=1
        if arr[i] == 0: #reset the counter 
            temp_counter = 0
        count = max(count,temp_counter)
    return count

print("2nd approach : ", second_approach(arr,n))