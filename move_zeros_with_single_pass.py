# We will use Swap in Place approach here

def move_zeros_swap(nums:list[int]) -> None:
    last_non_zero = 0 
    
    for i in range(len(nums)):
        if nums[i] != 0:
        
            # Swap current non-zero element into the target non-zero position
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1


nums = [0,1,0,3,12]
move_zeros_swap(nums)
print(nums)