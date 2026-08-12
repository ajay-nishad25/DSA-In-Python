

# brute force approach with time cmpx o(nlogn) + o(n)

def get_second_largest(arr):

    n = len(arr)
    if(n<=0):
        return -1
    
    arr.sort() # time cmpx is 0(n log n)
    print(arr)

    for i in range(n-2,-1,-1):  # time cmpx is 0(n)
        if arr[i] != arr[n-1] :
            return arr[i]
    return -1

arr = [12, 35, 1, 10, 34, 1, 23, 35]

print("second largest number in list is : ", get_second_largest(arr))

# 2 pass approach with time cpmx o(n) +o(n)

def approach_second(arr):

    n = len(arr)

    if n<=0:
        return -1
    
    largest = -1
    second_largest = -1

    # find the largest number 
    for i in range(n):
        if(arr[i]>largest):
            largest = arr[i]
    
    # 

    for i in range(n):
        if arr[i]>second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    return second_largest

print("second largest using approach 2 : ",approach_second(arr))

# approach 3 with time cpmx o(n)

def third_approach(arr):
    n = len(arr)
    if n<=0:
        return -1
    
    largest = arr[0]
    second_smallest = -1

    for i in range(n):
        if(arr[i]>largest):
            second_smallest = largest
            largest = arr[i]
        if arr[i]<largest and arr[i]>second_smallest:
            second_smallest = arr[i]
    return second_smallest

print("second largest using approach 3 : ",third_approach(arr))