# Shift all zeros to the end while keeping the order of the non-zero values. 
# Problem : Given an integer array nums, we need to move all the zeros to the end of it while maintaining the relative order of non-zero elements. 
# Intuition : We can use a two pointer approach
# Writer Pointer (last non-zero) ---> Tracks where the next non-zero number should be placed
# Reader Pointer (i) --> Scans through every element in the array

# As i scans the array, whenever it finds a non-zero element, it writes that value to nums[last_non_zero] and advances last_non_zero

# We will use Overwrite and Fill Method here

def move_zeros(nums:list[int]) -> None:
    last_non_zero = 0
    
    # Step 1 : Shift all non-zero elements to the front
    for i in range(len(nums)):
        # if current element is not 0, then swap places
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    
    # Step 2 : Fill the remaining indixes with 0s
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

nums = [0,1,0,3,12]
move_zeros(nums)
print(nums)