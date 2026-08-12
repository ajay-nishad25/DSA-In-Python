
# Bruteforce approach with time cmpx O(n) and space cmpx O(n)

arr = [1, 2, 3, 4, 5]

def brute_force(arr,n):

    if n<=0:
        print("invalid list")
        return None

    temp = [0]*n

    for i in range(1,n):
        temp[i-1] = arr[i]

    temp[n-1] = arr[0]
    return temp

approach_one_result = brute_force(arr,len(arr))
print("1st approach result : ",approach_one_result)

# approach 2 optimal solution with time cmpx O(n) and space O(1)
arr = [1, 2, 3, 4, 5]

def second_approach(arr,n):
    if n<=0:
        print("invalid list")
        return None

    element = arr[0]

    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = element
    print("inside fnx: ",arr)

second_approach(arr,len(arr))

# approach 3
arr = [1, 2, 3, 4, 5]

def slicing_approach(arr,n):
    if n<=0 :
        return None

    return arr[1:] + arr[:1]

result = slicing_approach(arr,len(arr))
print("3rd approach : ", result)