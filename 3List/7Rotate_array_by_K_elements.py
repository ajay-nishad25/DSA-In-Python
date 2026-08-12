
"""
Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


# approach 1 i.e brute force approach time cmpx O(n*k) + space O(k)

nums = [1,2,3,4,5,6,7]
k = 3

print("Approach 1st")
def first_approach(nums,k):

    """
    iteration 1: [7,1,2,3,4,5,6]
    iteration 2: [6,7,1,2,3,4,5]
    iteration 3: [5,6,7,1,2,3,4]
    """
    if k==0:
        print(nums)
        return nums
    n = len(nums)

    temp = nums[n-1]
    for i in range(n-1,0,-1):
        nums[i] = nums[i-1]
    nums[0] = temp
    first_approach(nums,k-1)



first_approach(nums,k)


nums = [1,2,3,4,5,6,7]

# approach 2 find modulo of k and array length
print("Approach 2nd")
def second_approach(nums,k):
    n = len(nums)
    k = k%n

    temp = [0]*n
    for i in range(n):
        if i<k:
            temp[i] = nums[n+i-k]
        else:
            temp[i] = nums[i-k]

    for i in range(n):
        nums[i] = temp[i]
    print(nums)

second_approach(nums,k)

# approach 3 
nums = [1,2,3,4,5,6,7]

print("Approach 3rd")
def third_approach(nums,k):
    n = len(nums)
    if n<=0:
        return
    k = k%n
    # 1st rotate last k elements
    nums[n-k:] = reversed(nums[n-k:])
    # rotate the initial element till n-k
    nums[:n-k] = reversed(nums[:n-k])
    # rotate the whole list
    nums[:]=reversed(nums)
    print(nums)

third_approach(nums,k)



nums = [1,2,3,4,5,6,7]
print("Approach 4th")
def fourth_approach(nums,k):
    n = len(nums)

    k=k%n

    temp = [0]*n

    for i in range(n):
        temp[(i+k)%n] = nums[i]

    print(temp)

fourth_approach(nums,k)

nums = [1,2,3,4,5,6,7]
print("temp approach")
def temp_approach(nums,k):
    k = k%len(nums)
    n = len(nums)

    temp= [0]*len(nums)

    for i in range(len(nums)):
        if i<k:
            temp[i] = nums[i+n-k]
        else:
            temp[i] = nums[i-k]
    print(temp)

temp_approach(nums,k)