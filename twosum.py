class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # We are given an array of integer nums and an integer target. Our goal is to find two indices i and j such
        # that nums[i] + nums[j] == target. Each input has exactly one solution and we cannot use the same element
        # twice. A brute force approach can be to check all pairs (i,j) of numbers and see if nums[i] + nums[j] ==
        # target and then return indices [i,j]. The time complexity in this case would be O(n^2) which is slow for 
        # large inputs. An optimal approach will be to use Hashmap. In this case, while iterating through the array, 
        # for each number num, we can check if the (complement = target - num) has been seen before and exists in
        # the dictionary.
        # Create a dictionary to store numbers  ---> index mapping
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num # complement is the number needed to reach target
            if complement in num_to_index:
                # If complement exists in dictionary, we found the 2 numbers that add upto target
                return [num_to_index[complement], i]
            # If complement doesn't exist --> Store current number with its index for future checks
            num_to_index[num] = i
        
        # Time Complexity - O(n)
        # Space Complexity - O(n)

