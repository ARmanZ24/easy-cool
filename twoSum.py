# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# Example: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] because nums[0] + nums[1] == 9

def two_sum(nums, target):
    # Creating a dictionary to store the difference of the target and each number
    num_map = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Checking if the complement (target - num) is already in the map
        complement = target - num
        if complement in num_map:
            # If true, return the indices
            return [num_map[complement], i]
        # If false, store the index of the current number in the map
        num_map[num] = i
    # Return an empty list if no solution is found
    return [] # Customize as you want like retun -1 for more operations

# read input
nums = list(map(int,input("Enter a list of positive numbers: ").split()))
target = int(input("Enter a positive target number: "))
result = two_sum(nums, target)
print("The indices are : ",result)