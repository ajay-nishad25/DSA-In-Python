"""
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
"""


arr = [2, 3, 5, -2, 7, -4]
n = len(arr)

# approach 1 bruteforce with time cpmx O(n^2) and space cmpx is O(1)

def first_approach(arr,n):

    max_sum = float("-inf")

    for i in range(n):
        max_subarray_sum = 0
        for j in range(i,n):
            max_subarray_sum += arr[j]
            max_sum = max(max_subarray_sum,max_sum)

    return max_sum

print("1st approach : ", first_approach(arr,n))


# approach 2 using kadane's algorithm 

def second_approach(arr,n):

    max_sum = 0
    current_max = 0

    for i in range(n):

        if current_max <= 0 :
            current_max = 0

        current_max += arr[i]
        max_sum = max(max_sum, current_max)

    return max_sum

print("2nd approach : ", second_approach(arr,n))