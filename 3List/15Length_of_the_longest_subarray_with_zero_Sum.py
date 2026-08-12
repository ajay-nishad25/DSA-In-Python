"""
Example 1:
Input:
N = 6, array[] = {9, -3, 3, -1, 6, -5}  
Result:
5  
Explanation:
The following subarrays sum to zero:
- {-3, 3}
- {-1, 6, -5}
- {-3, 3, -1, 6, -5}
The length of the longest subarray with sum zero is 5.

Example 2:
Input:
N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}  
Result:
8  
Explanation:
Subarrays with sum zero:
- {-2, 2}
- {-8, 1, 7}
- {-2, 2, -8, 1, 7}
- {6, -2, 2, -8, 1, 7, 4, -10}
The length of the longest subarray with sum zero is 8
"""

# approach 1 using brutforce approach
arr = [9, -3, 3, -1, 6, -5]
n = len(arr)

def first_approach(arr,n):

    max_length = 0

    for i in range(n):
        current_sum = 0
        for j in range(i,n):
            current_sum += arr[j]
            if current_sum == 0:
                # store the max length
                max_length = max(max_length, j-i+1)
    return max_length


print("1st approach : ",first_approach(arr,n))



# Optmial approach using prefixsum + hashmap approach


def second_approach(arr,n):

    prefix_sum = 0
    prefix_mapp ={}

    max_length = 0

    for i in range(n):

        prefix_sum += arr[i]

        if prefix_sum == 0:
            max_length = max(max_length,i+1)

        if prefix_sum in prefix_mapp : 
            max_length = max(max_length,i-prefix_mapp[prefix_sum])
        else:
            prefix_mapp[prefix_sum] = i

    return max_length

print("2nd approach : ", second_approach(arr,n))