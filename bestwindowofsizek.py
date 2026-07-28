# Problem : Given an array of integers nums and a positive integer k, find the maximum sum of any contiguous subarray (block) of size k.
# Goal : Find the maximum sum of k consecutive elements in O(N), avoiding recalculating the sum from scratch for every possible window size.

# Intuition : Imagine a window of size k sliding over the array from left to right
# 1. When the window slides one step to the right, one element exits on the left and one element enters on the right
# 2. Instead of resuming all the k elements, you can calculate the new sum in constant time O(1)
# The Formula : new_sum = current_sum - element_leaving + element_entering

def max_sum_array_of_size_k(nums: list[int], k:int) -> int:
    # Edge Case : If array has fewer elements than k, no valid window exists
    if len(nums) < k or k <= 0:
        return 0
    
    # Step 1: Compute the sum of very first window of size k
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Step 2: Slide the window from index k to the end of the array
    for i in range(k, len(nums)):
        # Subtract element leaving/sliding out nums[i-k]
        # Add elements entering nums[i]
        
        window_sum = window_sum + nums[i] - nums[i-k]
        
        # Track the maximum sum encountered
        max_sum = max(max_sum,window_sum)
    
    return max_sum

nums = [2,1,5,1,3,2]
k = 3
print(max_sum_array_of_size_k(nums,k))