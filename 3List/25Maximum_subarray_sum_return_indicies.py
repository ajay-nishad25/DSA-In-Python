"""
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: [3,6]
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.


Input: arr[] = [5, 4, 1, 7, 8]
Output: [0,4]
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
"""


# approach 1 with time cmpx O(n^2) and space cmpx O(1)

arr = [2, 3, -8, 7, -1, 2, 3]
n = len(arr)

def first_approach(arr,n):

    max_sum = float("-inf")
    start = 0
    end = 0

    for i in range(n):
        max_subarray_sum = 0
        for j in range(i,n):
            max_subarray_sum += arr[j]
            if max_subarray_sum>max_sum:
                max_sum = max(max_subarray_sum,max_sum)
                start = i
                end = j

    return [start,end]

print("1st approach : ", first_approach(arr,n))



# approach 2 using kadanes alogrithm

def second_approach(arr,n):

    max_sum = float("-inf")
    current_sum = 0
    ansStart = -1
    ansEnd = -1
    start = 0

    for i in range(n):
        if current_sum == 0:
            start = i
        
        current_sum += arr[i]

        if current_sum>max_sum:
            max_sum = current_sum
            ansStart = start
            ansEnd = i

        if current_sum < 0:
            current_sum = 0

    return [ansStart,ansEnd]

print("2nd approach : ", second_approach(arr,n))

