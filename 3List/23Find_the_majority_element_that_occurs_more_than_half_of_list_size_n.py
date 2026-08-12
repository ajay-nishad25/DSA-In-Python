"""
Example 1:
Input:
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output:
7  
Explanation:
The number 7 appears 5 times in the 9-sized array, making it the most frequent element.

Example 2:
Input:
nums = [1, 1, 1, 2, 1, 2]  
Output:
1  
Explanation:
The number 1 appears 4 times in the 6-sized array, making it the most frequent element.
"""

# 1st approach

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
n = len(arr)

def first_approach(arr,n):

    max_count = 0
    majority_element = None

    for i in range(n):
        inner_count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                inner_count+=1
        if max_count<inner_count:
            # found the most repetative element count
            majority_element = arr[i]
print("1st approach : ",first_approach(arr,n))



# 2nd approach oprimizing the first approach 
"""
since the first approach running form O(n*n) ineO(n^2) in all best worst and averga case
since we are finding the largest/majority element whos is element>n/2 so simply check this so it would be O(n*logn) in best and average case

"""

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
n = len(arr)

def second_approach(arr,n):
    for i in range(n):
        inner_count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                inner_count+=1
        print("inner count",inner_count)
        if inner_count>n//2:
            # found the most repetative/majority element count
            return arr[i]


print("optimizing the 1st approach : ",second_approach(arr,n))


# 3rd approach

def third_approach(arr,n):
    temp_hash = dict()

    for i in range(n):
        temp_hash[arr[i]] = temp_hash.get(arr[i],0)+1

    print(temp_hash)

    majority_element = max(temp_hash, key=temp_hash.get)
    print(majority_element)

third_approach(arr,n)



# 4th approach with time cmpx O(n) and space cmps O(1)

arr = [1,1,1,2,2,2]  
n = len(arr)

def fourth_approach(arr,n):

    count = 0
    candidate = -1

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count+=1
        else:
            count-=1

    count = 0
    for num in arr:
        if num == candidate:
            count+=1

    if count>n//2:
        return candidate
    else:
        return -1

print("4th optimal approach : ", fourth_approach(arr,n))