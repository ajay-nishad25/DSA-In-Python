
"""
Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
Output : YES
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].

Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
Output : NO.
Explanation: There exist no such two numbers whose sum is equal to the target. 
"""


# approach 1 bruteforce approach

arr = [2,6,5,8,11]
n = len(arr)
target = 14

def first_approach(arr,n,target):

    for i in range(n):
        for j in range(n):
            if arr[i]+arr[j] == target:
                return True

    return False

print("1st approach : ", first_approach(arr,n,target))

# approach 2 better approach with time cmpx O(nlog(n)) for sort and O(n for traverse * log(n) for binary search)and space cmpx is O(n)

"""
approach sort the array and put pointer on 1st index and move accordingly and subtract the target- arr[i] 
and find the resultant element in array using binary search 
"""

arr = [2,6,5,8,11]
n = len(arr)
target = 14


def binary_search(arr,n,target):
    start = 0
    end = n-1

    while(start<=end):
        mid = start+(end-start)//2
        if arr[mid] == target:
            return True
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1

    return False

def second_approach(arr,n,target):

    arr.sort()

    for i in range(n):

        element = arr[i]

        if binary_search(arr,n,target-element):
            return True
    return False

print("2nd approach : ", second_approach(arr,n,target))


# approach 3 optimal approach with time cpmx O(n*logn) for sort + O(n) for traverse

def third_approach(arr,n,target):

    arr.sort()

    start = 0
    end = n-1

    while (start<=end):

        sum = arr[start] + arr[end]

        if sum == target:
            return True
        elif sum > target:
            end -=1
        else:
            start +=1
    return False

print("3rd approach : ", third_approach(arr,n,target))


# Alternate approach using hashset i.e set

def set_approach(arr,n,target):

    temp_set = set(arr)

    print(temp_set)

    for (i,element) in enumerate(arr):
        pending = target-element
        print("pending element : ",pending)
        if pending in temp_set:
            return True

    return False

print("4th approach using set/hashset : ",set_approach(arr,n,target))


# Alternate approach using hashmap i.e dict

def dict_approach(arr,n,target):

    temp_dict = {}

    for (i,value)in enumerate(arr):
        pending = target - value
        if pending in temp_dict:
            return True
        temp_dict[pending] = i
    return False

print("5th approach : ",dict_approach(arr,n,target))


