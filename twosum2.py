# Two Sum Problem:
# Given an array of integers and a target,
# we need to return the indices of the two numbers that add up to the target.

def twosum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        x = target - num
        print(f"At index {index}, we have number {num} and the complement is {x} that adds up to {target}")

        # Check if the complement exists
        if x in hashmap:
            return [hashmap[x], index]

        # If it does not exists, Store the current number and its index
        hashmap[num] = index

nums = [2, 7, 11, 15]
target = 9

print(twosum(nums, target))