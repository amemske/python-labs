# Question
# Consider a scenario where you have been given a list of integers representing the daily stock prices of a company for a given period.
# You are also provided with a set or dictionary of stock prices for the same period. You are required to implement a program that performs the following tasks:


stock_prices_list = [50, 55, 60, 54, 92]
stock_prices_set = { 100, 200, 300, 700}
stock_prices_dict = {0: 500, 1:550, 2: 600, 3:450, 4:510}




# Calculate the average stock price:
# Write a method, calculateAveragePrice, that takes the list of stock prices as input and returns the average price of the stocks.

def calculateAveragePrice(stock_prices_list):
    if not stock_prices_list:
        return 0 # return 0 if empty
    total = sum(stock_prices_list)
    average = total / len(stock_prices_list)
    return average

# Write a function, findMaximumPrice, that takes the list of stock prices as input and returns the maximum price among all the stocks.
# Determine the occurrence count of a specific price:

def findMaximumPrice(stock_prices_list):
    if not stock_prices_list:
        return 0
    maxPrice = max(stock_prices_list)
    return maxPrice



# Write a function, countOccurrences, that takes the list of stock prices and a target price as input and returns the number of times the target
# price occurs in the list.
# Compute the cumulative sum of stock prices:

def countOccurrences(stock_prices_list, target_price):
    return stock_prices_list.count(target_price)

# Write a function, computeCumulativeSum, that takes the set or dictionary of stock prices as input and returns a new set or dictionary containing
# the cumulative sum of prices at each position.
def computeCumulativeSum(stock_prices_set):

    if not stock_prices_set:
        return {}
    
    cumulative_sum_container = {}
    sum = 0
    for i, price in enumerate(stock_prices_set):
        sum +=price
        cumulative_sum_container[i] = sum
    
    return cumulative_sum_container


print("Average Price", calculateAveragePrice(stock_prices_list))
print("Maximum Price", findMaximumPrice(stock_prices_list))
target_price = 60
print("count Occurrences", countOccurrences(stock_prices_list, target_price))
print("Computed Sum", computeCumulativeSum(stock_prices_set))
