"""
FOR POSITIVES NUMBERS ONLY
Example 1:
Input:
nums = [10, 5, 2, 7, 1, 9], k = 15  
Output:
4  
Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Example 2:
Input:
nums = [-3, 2, 1], k = 6  
Output:
0  
Explanation:
There is no sub-array in the array that sums to 6. Therefore, the output is 0.
"""


# approach 1 bruteforce approach


nums = [10, 5, 2, 7, 1, 9]
k = 15

def first_approach(nums,k):

    count = 0
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if sum == k:
                count = max(count,j-i+1)

    return count

print("1st approach : ", first_approach(nums,k))


# approach 2

nums = [10, 5, 2, 7, 1, 9,1,2,1,1,1,-30]
k = 15

def second_approach(nums,k):
    max_count = 0
    left=0
    right=0
    sum = nums[0]
    n = len(nums)
    while right<n:

        # increment left until its sum becomes less than k
        while sum>k and left<=right:
            sum -= nums[left]
            left += 1

        
        if sum == k:
            max_count = max(max_count,right-left+1)

        right +=1
        if right<n:
            sum += nums[right]
        

    return max_count


print("2nd approach : ", second_approach(nums,k))
