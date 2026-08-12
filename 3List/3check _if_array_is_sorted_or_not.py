



# Brute-force approach

arr = [1,2,2,3,4,5,]


def first_approach(arr):
    n = len(arr)
    if n<=0 :
        return False

    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                return False

    return True



print("is array sorted : ", first_approach(arr))


# Optimal-Approach 

def is_sorted(arr):
    n = len(arr)
    if n <= 1:
        return True
    
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True

print("is array sorted : ",is_sorted(arr))

