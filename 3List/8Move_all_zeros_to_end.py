"""
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
"""


# approach 1 brute force time cmpx O(n) + space O(n)

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)

def first_approach(arr,n):
    temp = [0]*n
    index = 0
    for i in range(n):
        if arr[i] != 0:
            temp[index] = arr[i] 
            index +=1
    print("first approach result : ", temp)

first_approach(arr,n)

# approach 2 optimal approach with 2 pointer approach

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)

def second_approach(arr,n):

    for i in range(n):
        if arr[i] == 0:
            for j in range(i+1,n):
                if arr[j] != 0:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
    print("second approach result : ", arr)
                    

second_approach(arr,n)


# optimizing the above approach 

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)


def third_approach(arr,n):
    pointer = -1
    # find the 1st 0th element
    for i in range(n):
        if arr[i] == 0:
            pointer = i
            break
    # now uisng pointer swap all element with pointer which are non-zero

    for i in range(pointer+1,n):
        if arr[i] != 0:
            arr[pointer],arr[i] = arr[i],arr[pointer]
            pointer +=1
    print("optimize approach : ", arr)

third_approach(arr,n)


arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)

# def fourth_approach(arr,n):

#     for i in range(n):
#         if arr[i] ==0:
#             for j in range(i+1,n):
#                 if arr[j] != 0:
#                     arr[i],arr[j]=arr[j],arr[i]
#                     break

#     print(arr)

# fourth_approach(arr,n)

# approach 4th shift all non-zeros to front

def fourth_approach(arr,n):
    pointer = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[pointer]=arr[pointer],arr[i]
            pointer +=1
    print(arr)
fourth_approach(arr,n)