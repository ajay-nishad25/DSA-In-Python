"""
Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
Output: [1,2,3,4,_,_,_,_,_,_,_]
Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
"""



arr = [1,1,1,2,2,3,3,3,3,4,4]


# approach 1: bruteforce approach 

def first_approach(arr):
    seen = set()
    index = 0

    for num in arr:
        if num not in seen:
            seen.add(num)
            arr[index]=num
            index += 1

    print(seen)
    print(arr)

first_approach(arr)

print(arr)

# approach 2 : time cmpx is O(n) space is O(n)

def second_approach(arr):
    result = []

    n = len(arr)
    i = 0

    while i<n:
        result.append(arr[i])
        j = i+1
        while j<n and arr[i]==arr[j]:
            j+=1
        i = j

    print(result)

first_approach(arr)
