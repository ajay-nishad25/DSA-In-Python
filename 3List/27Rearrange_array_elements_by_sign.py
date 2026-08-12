"""
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Example 1:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.




Example 2:
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 
Positive elements = 1,2,3
Negative elements = -3,-1,-2
To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
Also, -3 should come before -1, and -1 should come before -2.

"""


arr = [1,2,-4,-5]
n = len(arr)


# 1st approach using 2 seperate array for postive and negative number along with resultant array

def first_approach(arr,n):
    # 1st approach using dual array
    half = n//2
    postive_list = []*half
    negative_list = []*half
    
    for i in range(n):
        if arr[i]>0:
            postive_list.append(arr[i])
        else:
            negative_list.append(arr[i])
    
    flag = True
    index = 0
    positive_index = 0
    negative_index = 0

    while index<n:
        if flag:
            arr[index] = postive_list[positive_index]
            positive_index += 1
            index += 1
            flag=False
        else:
            arr[index] = negative_list[negative_index]
            negative_index += 1
            index += 1
            flag=True
    return arr

print("1st approach : ", first_approach(arr,n))



# approach 2 

def second_approach(arr,n):

    result = [0]*n
    positive_index = 0
    negative_index = 1

    for i in range(n):

        if arr[i]>0: # positive number so put this at even index
            result[positive_index] = arr[i]
            positive_index +=2
        else:
            result[negative_index] = arr[i]
            negative_index +=2

    return result

print("2nd approach : ", second_approach(arr,n))
