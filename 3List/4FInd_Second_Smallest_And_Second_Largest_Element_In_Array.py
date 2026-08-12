"""
Input:
[1, 2, 4, 7, 5]  
Output:
Second Smallest : 2  
Second Largest : 5  
Explanation:
The elements are sorted as 1, 2, 4, 5, 7.
Hence, the second smallest element is 2, and the second largest element is 5.
"""


# approach 1 brute force approach time cmpx O(nlogn)

arr=[1,2,4,7,5,8]
print("1st approach")
def first_approach(arr):
    n = len(arr)
    if n<=0 or n<=1:
        print(-1,-1)

    arr.sort()
    print("2nd smallest : ", arr[1])
    print("2nd largest : ", arr[n-2])

first_approach(arr)


# approach 2 better approach O(n)+O(n)
"""
approach:
1st find the smallest and largest
2nd then using the smallest find the 2nd smallest which is just greater than smallest
3rd then using the largest find the 2nd largest which is just smaller than the largest
"""
print("2nd approach")
def second_approach(arr):
    n = len(arr)
    if n<=0 or n<=1:
        print(-1,-1)

    smallest = float("inf")
    largest = float("-inf")

    for i in range(n):
        if arr[i]>largest:
            largest = arr[i]
        if arr[i]<smallest:
            smallest = arr[i]

    second_largest = float("-inf")
    second_smallest = float("inf")

    for i in range(n):
        # find second largest
        if arr[i] != largest and second_largest < arr[i]:
            second_largest = arr[i]
        # find second smallest
        if arr[i] != smallest and second_smallest > arr[i]:
            second_smallest = arr[i]

    print("2nd smallest value is : ", second_smallest)
    print("2nd largest value is : ", second_largest)

second_approach(arr)

# approach 3 optimal approach 
print("3rd approach")
def third_approach(arr):
    n = len(arr)
    if n<=0 or n<=1:
        print(-1,-1)

    smallest = float('inf')
    largest = float('-inf')
    second_smallest = float('inf')
    second_largest = float('-inf')

    for i in range(n):
        # for second largest
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        if arr[i] != largest and arr[i]>second_largest:
            second_largest = arr[i]

        # for second smallest
        if arr[i]<smallest:
            second_smallest = smallest
            smallest = arr[i]
        if arr[i]!=smallest and arr[i]<second_smallest:
            second_smallest = arr[i]

    print("2nd smallest value is : ", second_smallest)
    print("2nd largest value is : ", second_largest)

third_approach(arr)
