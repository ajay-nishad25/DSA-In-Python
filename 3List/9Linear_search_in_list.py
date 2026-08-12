arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)

def linear_search(arr,n,k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

print("Element present at index : ", linear_search(arr,n,3))