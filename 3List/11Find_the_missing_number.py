
"""
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
"""

# approach 1 bruteforce approach with time cmpx is O(n^2) and space O(1)

arr = [8, 2, 4, 5, 3, 7, 1]
n = len(arr)

def first_approach(arr,n):

    for i in range(1,n+1):
        found = True
        for j in range(n):
            if i == arr[j]:
                found = False

        if found:
            return i

    return -1

print("This number is missing : ",first_approach(arr,n))

# approach 2 better approach time cmpx O(nlogn)+O(n) and space cmpx is O(1)

def second_approach(arr,n):
    arr.sort()

    counter = 1
    for i in range(0, n+1):
        if arr[i] == counter:
            counter +=1
        else:
            return counter

    return -1

print("This number is missing 2nd approach : ",second_approach(arr,n))

# approach 3 
arr = [8, 2, 4, 5, 3, 7, 1]
n = len(arr)

def third_approach(arr,n):
    hash = [0]*(n+1)

    for i in range(n):
        hash[arr[i]-1] = 1

    for i in range(len(hash)):
        print(i)
        if hash[i] != 1:
            return i+1
    return -1

print("This number is missing 3rd approach : ",third_approach(arr,n))



# approach 4
arr = [8, 2, 4, 5, 3, 7, 1]
n = len(arr) 
def fourth_approach(arr,n):
    sum =0
    n = n+1
    for i in arr:
        sum +=i

    expected_sum = n * (n+1)//2
    print(sum)
    print(expected_sum)
    return expected_sum-sum

print("This number is missing 4th approach : ",fourth_approach(arr,n))


# approach 5

arr = [8, 2, 4, 5, 3, 7, 1]
n = len(arr) 


def fifth_approach(arr,n):
    xor1 = 0
    xor2 = 0

    for i in range(1,n+2):
        xor1 ^= i

    for i in arr:
        xor2^= i

    temp = 0
    for i in range(n):
        temp ^= arr[i]
        temp ^= (i+1)

    print("this is optmized way using single loop ",temp^(n+1))


    return xor1^xor2


print("This number is missing 5th approach : ",fifth_approach(arr,n))
