"""

Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note: That buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


# approach 1 bruteforce with time O(n^2)
arr = [7,6,4,3,1]
n = len(arr)

def first_approach(arr,n):

    # profit = sell - buy
    max_profit = 0
    for i in range(n):
        for j in range(i+1,n):
            max_profit = max(max_profit,arr[j]-arr[i])

    return max_profit

print("1st approach : ", first_approach(arr,n))



# approach 2

def second_approach(arr,n):

    min_element = arr[0]
    profit = float("-inf")

    for i in range(n):
        min_element = min(min_element, arr[i])
        profit = max(profit, arr[i]-min_element)
    return profit

print("2nd approach : ", second_approach(arr,n))


