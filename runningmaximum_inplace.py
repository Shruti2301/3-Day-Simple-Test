# This approach modifies the original list directly, reducing extra memory usage to O(1)

def running_maximum_in_place(nums: list[int]) -> list[int]:
    # Edge Case : Empty lists or single elements list need no processing
    
    if len(nums) <= 1:
        return nums
    
    # Start from index 1 because the element at index 0 is already runnning its own marathon
    for i in range(1, len(nums)):
        # If current element is smaller than the previous element overwrite current element with that max value
        if nums[i] < nums[i-1]:
            nums[i] = nums[i-1]
            
            # If nums[i] >= nums[i-1], it is a new maximum, so new change is needed
    return nums

nums = [3,1,4,1,5]
print(running_maximum_in_place(nums))