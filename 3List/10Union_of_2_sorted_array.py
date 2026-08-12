"""
Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
Output: {1,2,3,4,5}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}

Input:n = 10,m = 7,arr1[] = {1,2,3,4,5,6,7,8,9,10} arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}
"""

# approach 1 using map i.e dict

arr1 = [1,2,3,4,5,6,7,8,9,10]
n = len(arr1)
arr2 = [2,3,4,4,5,11,12]
m = len(arr2)

def first_approach(arr1,n,arr2,m):

    result_map = {}

    for num in arr1:
        result_map[num] = 1

    for num in arr2:
        result_map[num] = 1

    return list(result_map)

result = first_approach(arr1,n,arr2,m)
print("1st approach : ",result)

# approach 2 using set
arr1 = [1,2,3,4,5,6,7,8,9,10]
n = len(arr1)
arr2 = [2,3,4,4,5,11,12]
m = len(arr2)

def second_approach(arr1,n,arr2,m):
    result_set = set()

    for num in arr1:
        result_set.add(num)
    for num in arr2:
        result_set.add(num)

    return list(result_set)

result = second_approach(arr1,n,arr2,m)
print("2nd approach : ",result)

# approach 3 using 2 pointer approach with time cmpx O(n+m) and space O(n+m)
arr1 = [1,2,3,4,5,6,7,8,9,10]
n = len(arr1)
arr2 = [2,3,4,4,5,11,12]
m = len(arr2)

def third_approach(arr1,n,arr2,m):
    i,j=0,0

    result = []

    while i<n and j<m:

        if arr1[i]<arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i +=1
        elif arr1[i]>arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j +=1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
                i +=1
                j +=1

    # if j is still pending 
    while j<m:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j +=1 

    # if i is still pending
    while i<n:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i +=1

    return result

result = third_approach(arr1,n,arr2,m)
print("3rd optimal approach : ",result)