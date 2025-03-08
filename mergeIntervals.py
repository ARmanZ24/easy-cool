# Problem: Given a collection of intervals, merge any overlapping intervals.
# Example: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge_intervals(intervals):
    # Sort intervals by the start value of each
    intervals.sort(key=lambda x: x[0])
    
    # Starting with an empty result list
    merged = []
    
    for interval in intervals:
        # If the merged list is empty or there's no overlap, just adding the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # If false, there's an overlap, so intervals to be merged
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

def get_intervals_input():
    intervals = []
    
    # Asking the user for the number of intervals
    num_intervals = int(input("Enter the number of intervals: "))
    
    # Get the intervals from the user
    for i in range(num_intervals):
        # For each interval, expecting input in the format: start,end
        interval_str = input(f"Enter interval {i+1} (format: start,end): ")
        
        # Spliting the input string by comma and convert to integers
        start, end = map(int, interval_str.split(","))
        
        # Appending the interval as a list [start, end]
        intervals.append([start, end])
    
    return intervals

# Get intervals from the user
intervals = get_intervals_input()

# Merging intervals and printing out the results
result = merge_intervals(intervals)
print("Merged intervals are:", result)