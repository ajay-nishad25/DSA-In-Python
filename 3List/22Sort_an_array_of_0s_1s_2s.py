"""
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero two's.
"""

# approach 1 bruteforce approach time cmpx is o(n^2) and space cpmx O(1)

arr = [1, 0, 2, 1, 0]
n = len(arr)

def first_approach(arr,n):

    for i in range(n):
        index=i
        for j in range(i+1,n):
            if arr[j]<arr[index]:
                index = j
        arr[i],arr[index]=arr[index],arr[i]
    return arr

print("1st approach : ", first_approach(arr,n))


# approach 2 using count i,e count 0, 1 and 2 and replace the original array


arr = [1, 0, 2, 1, 0]
n = len(arr)

def second_approach(arr,n):

    zero, ones, twos = 0,0,0

    for i in range(n):
        if arr[i] == 0:
            zero+=1
        elif arr[i] == 1:
            ones+=1
        else:
            twos+=1

    for i in range(n):
        if zero != 0:
            arr[i] = 0
            zero-=1
        elif ones!=0:
            arr[i] = 1
            ones-=1
        else :
            arr[i] = 2
            twos-=1

    return arr

print("2nd approach : ", second_approach(arr,n))


# approach 3 using 3 pointers approach with time O(n) and space cmpx O(1)

arr = [2, 0, 2, 1, 1, 0]
n = len(arr)
def third_approach(arr,n):

    s,m,e= 0,0,n-1

    while m<=e:
        if arr[m] == 0:
            arr[m],arr[s] = arr[s],arr[m]
            m+=1
            s+=1
        elif arr[m] == 1:
            arr[m],arr[s] = arr[s],arr[m]
            m+=1
        else:
            arr[m],arr[e] = arr[e],arr[m]
            e-=1

    return arr

print("3rd approach : ", third_approach(arr,n))

arr = [2,0,2,1,1,0]
n = len(arr)

def same_third_approach(arr,n):

    s,m,e= 0,n-1,n-1

    while m>=s:
        if arr[m] == 0:
            arr[m],arr[s] = arr[s],arr[m]
            s+=1
        elif arr[m] == 1:
            m-=1
        else:
            arr[m],arr[e] = arr[e],arr[m]
            m-=1
            e-=1
    return arr

print("3rd approach : ", same_third_approach(arr,n))