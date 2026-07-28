# We need to return a new list of the same length when the element at index i is simply max(running_max,current_element)
# Goal : Compute the cumulative maximum at every step in single pass O(N) without rescanning the subarray for position O(N^2) time.

# Intution:
# We can keep track of our 'personal best' score as we play the game
# 1. As we move thorugh the list from left to right, we need to think about :
# --> What was the highest value seen so far?
# --> Is the current element nums[i] larger than the highest value?
# 2. The maximum upto index i is simply max(running_max,current_element)
# 3. By storing and updating this running_max value as we iterate, we can avoid reevaluating other elements

def running_maximum(nums: list[int]) -> list[int]:
    # Edge Case : Handle the empty list gracefully
    if not nums:
        return []
    result = []
    
    # Initialize with the smallest possible float
    current_max = float('-inf')
    
    # Traverse each number in array sequentially
    for num in nums:
        # Update the max seen so far by comparing it with the current number
        current_max = max(current_max, num)
        
        # Append the highest value found upto this index to our output list
        result.append(current_max)
    
    return result

nums = [3,1,4,1,5]
print(running_maximum(nums))