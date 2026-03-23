# Problem: Two Sum
# Pattern: Hashing

# Approach:
# Use a hashmap to store visited numbers and their indices.
# For each element, check if (target - current) exists.

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in hashmap:
            return [hashmap[needed], i]

        hashmap[nums[i]] = i
