# Given a sorted list of integers nums and an integer target, return the 0-based index of target if it exists in nums. If not present, return -1

# Since the array is already sorted, we can repeatedly divide the search range in half
# 1. Compare the target with the element in the middle of the range(mid)
# 2. If nums[mid] == target, we found it. Return mid 
# 3. if nums[mid] > target, the target must lie in the left half (all the elements to the right are larger)
# 4. if nums[mid] < target, the target must be in the right half (all the elements to the left are smaller)
# 5. Keep narrowing the bounds (left and right) until we find the target or search range becomes invalid

def binary_search(nums: list[int], target:int) -> int:
    # Initialize pointer boundaries for the entire list
    left = 0 
    right = len(nums) - 1
    
    # Continue searching as long as search range in valid
    while left <= right:
        # Calculate middle index
        mid = left + (right - left) // 2
        
        # Case 1 : Target found at middle
        if nums[mid] == target:
            return mid
        
        # Case 2 : Target is larger than the middle, so we discard left half
        elif nums[mid] < target:
            left = mid + 1
        
        # Case 3 : Target is smaller than the middle, so we discard the right half
        else: 
            right = mid - 1
    
    # Target was not found in the array
    return -1

nums = [1,3,5,7,9]
target = 7
print(binary_search(nums,target))