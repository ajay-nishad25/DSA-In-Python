

# approach 1 with time cpmx o(nlogn) 

def largets_element(arr):
    n = len(arr)
    if n<=0 :
        return -1
    arr.sort()
    return arr[n-1]    



arr = [12, 35, 1, 10, 34, 1, 23, 35]

print("largest element in list is : ",largets_element(arr))


# approach 2 with time cpmx o(n)

def second_approach(arr):
    n = len(arr)
    if n<=0:
        return -1
    
    largest = -1

    for i in range(n):
        if(arr[i]>largest):
            largest = arr[i]
    
    return largest

print("largest element in list is : ",second_approach(arr))

