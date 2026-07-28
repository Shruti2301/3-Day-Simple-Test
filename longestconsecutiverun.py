# Given unsorted integers, return the length of the longest run of consecutive numbers. Aim for O(n) — no sorting.

# Example: [100,4,200,1,3,2] → 4 (the run 1,2,3,4)

def longestConsecutive(nums):
    # Step 1 : Handle the empty list edge case (if there are no elements in the list ==> return 0)
    if not nums:
        return 0
    
    # Step 2 : Convert the list into a set
    numSet = set(nums)
    
    # Step 3 : This will track the longest chain length found so far
    longestStreak = 0
    
    # Step 4 : Loop through every number in the set (Each number visited once)
    for num in numSet:
        # Step 5: Only start counting a new chain if 'num' is a TRUE starting point.
        if num - 1 not in numSet:
            currentNum = num  # Start Walking from this number
            currentStreak = 1     # The starting number itself counts as length 1
        
            # Step 6 : Keep walking forward (num + 1, num + 2, num + 3)
            while currentNum + 1 in numSet:
                currentNum += 1     # Move to the next number in the chain
                currentStreak += 1  # Increase the length of this chain
            
            # Step 7 : Update the overall longest streak if this chain is longer
            longestStreak = max(longestStreak, currentStreak)
    
    # Step 8 : Return the length of the longest consecutive chain found
    return longestStreak

print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Expected output: 4

            