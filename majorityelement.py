def majorityElement(nums):
    # Step 1: Create an empty dictionary to store frequency counts.
    # Key = the number itself, Value = how many times it has appeared so far.
    countMap = {}
    
    # Step 2: Store the total number of elements in the list.
    # This is used to calculate the majority threshold (n // 2).
    n = len(nums)
    
    # Step 3: Loop through every element in the input list, one at a time.
    for num in nums:
        
        # Step 4: Update the count for the current number.
        # countMap.get(num, 0) looks up the current count for 'num'.
        #   - If 'num' has been seen before, it returns its existing count.
        #   - If 'num' has never been seen, it returns 0 (the default).
        # We then add 1 to account for this current occurrence,
        # and store the updated count back into the dictionary.
        countMap[num] = countMap.get(num, 0) + 1
        
        # Step 5: Check if this number has now become the majority element.
        # A majority element must appear MORE THAN n // 2 times.
        # We check this immediately after every update (not after the full loop)
        # so we can exit early as soon as we find the answer.
        if countMap[num] > n // 2:
            
            # Step 6: Return the number immediately — no need to keep scanning
            # the rest of the list, since only one majority element can exist.
            return num

# Step 7: Call the function with a sample list and print the result.
# In [2, 2, 1, 1, 1], the number 1 appears 3 times out of 5 elements,
# which is more than 5 // 2 = 2, so 1 is the majority element.
print(majorityElement([2, 2, 1, 1, 1]))