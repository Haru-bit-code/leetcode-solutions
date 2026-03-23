# Problem: Contains Duplicates

# Problem
Given an integer array `nums`, return `true` if any value appears at least twice.

# Approach
- Use a set to track seen elements
- If element repeats → return True

# Complexity
- Time: O(n)
- Space: O(n)



def containsDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
