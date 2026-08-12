
"""
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.


Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""


# approach 1 bruteforce approach with time cmpx O(n^2) and space O(1)

arr = [8, 8, 4, 5, 5, 7, 7]
n = len(arr)

def first_approach(arr,n):

    for i in range(n):
        found = True
        for j in range(n):
            if arr[i]==arr[j] and i!=j:
                found = False
                break
        if found:
            return arr[i]
    return -1

print("1st approach : ", first_approach(arr,n))

# approach 2 better approach with time cmpx O(n)+O(n) and space O(n)

def second_approach(arr,n):
    hash_map = dict()
    for i in range(n):
        hash_map[arr[i]] = hash_map.get(arr[i],0)+1
    print(hash_map)

    min_count = float("inf")
    smalles_key = None
    for (key,value) in hash_map.items():
        if value < min_count:
            min_count = value
            smalles_key = key
    return smalles_key

print("2nd approach : ", second_approach(arr,n))


# approach 3 optimial approach with time O(n) and space O(1)

def third_approach(arr,n):

    xor = 0

    for i in range(n):
        xor ^= arr[i]

    return xor

print("3rd approach : ", third_approach(arr,n))


############################# Extra un-optimized code

# 4th approach with time cmpx O(nlogn)
arr = [8, 8, 4, 4, 6, 5, 5, 7, 7]
n = len(arr)

def fourth_approach(arr,n):

    arr.sort()
    # [4, 4, 5, 5, 6, 7, 7, 8, 8]

    i = 0
    while i<n:
        if arr[i]!= arr[i+1]:
            return arr[i]
        i +=2

    return -1

print("4th approach : ", fourth_approach(arr,n))

# 5th approach
arr = [8, 8, 4, 4, 6, 5, 5, 7, 7]
n = len(arr)

def fifth_approach(arr,n):
    sum_of_unique = 0
    unique_set = set(arr)
    for i in unique_set:
        sum_of_unique += i

    sum_of_all = 0
    for i in arr:
        sum_of_all += i

    return (2*sum_of_unique)-sum_of_all

print("5th approach : ", fifth_approach(arr,n))