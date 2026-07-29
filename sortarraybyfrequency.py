# Sort numbers so that the most frequent come elements come first.

# Problem : Given an array of integer nums, sort the array based on the frequency of the values in descending order (most frequent elements first). 
# If two elements have the same frequency, sort them by their numerical value in ascending order. 

# Goal : Group and count the frequency of each number, then custom sort the unique elements using a compound key (-frequency, value)

# 1. Count how many times each number appears using a hashmap or Python's Collection Counter
# 2. Primary Rule : Frequency (Descending) : Higher count comes first. In Python, we do the (-frequency) when sorting ascending value by default
# 3. Secondary Rule (Tie Breaker) : Value (Ascending) smaller number goes first 
# 4. Set the unique numbers using this tuple key. (-frequency, value)
# 5. Reconstruct the first list by repeating each number according to the count

from collections import Counter

def frequency_sort(nums:list[int]) -> list[int]:
    # Step 1 : Count frequencies of each number
    # Example : [4,4,1,2,2,3] ---> Counter ({4:2, 2:2, 1:1, 3:1})
    counts = Counter(nums)
    
    # Step 2 : Sort original list directly using Custom key
    # Key (-counts[x],x) means:
    # - First Priority : Higher Frequency
    # - Second Priority : Smaller Value X
    
    
    # The key parameter tells python .sort() function to evaluate a custom rule for every item x in nums before making comparisons
    nums.sort(key = lambda x: (-counts[x],x))
    
    return nums

nums = [4,4,1,2,2,3]
print(frequency_sort(nums))