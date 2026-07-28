def max_subarray_of_size_k_with_window(nums: list[int], k:int) -> tuple[int,list[int]]:
    
    # Edge Case: If array has fewer elements, no valid window exists
    if len(nums) < k  or k <= 0:
        return 0, []
    
    # Step 1 : Compute the sum of the first window (indices 0 to k - 1)
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Track the starting index of maximum window found so far
    best_start_idx = 0
    
    # Step 2 : Slide window from from index k to end of the array
    for i in range(k, len(nums)):
        # Subtract the element leaving (nums[i-k])
        # Add the new element (nums[i])
        window_sum += nums[i] - nums[i-k]
        
        # Update maximum sum and save the new window's starting index
        if window_sum > max_sum:
            max_sum = window_sum
            # Current window starts at i-k+1
            best_start_idx = i - k + 1
    
    # Step 3 : Slice the array from best_start_idx to best_start_idx + k to get the window
    
    best_window = nums[best_start_idx : best_start_idx + k]
    
    return max_sum, best_window

nums = [2,1,5,1,3,2]
k = 3

max_sum, window = max_subarray_of_size_k_with_window(nums,k)

print(f"Maximum Sum: {max_sum}")
print(f"Window: {window}")