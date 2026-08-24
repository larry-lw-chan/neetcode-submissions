import math


class Solution:
    def search(self, nums: list[int], target: int):
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums: list[int], target: int, s: int, e: int):
        # Base Case
        if e - s + 1 <= 1:
            if nums[e] == target:
                return e  # do final check
            else:
                return -1  # no numbers match

        m = (e + s) // 2  # Get middle

        # Return Target if found
        if target == nums[m]:
            return m
        # Process lower half if target is lower than midpoint
        if target < nums[m]:
            return self.binary_search(nums, target, s, m)

        # Process lower half if target is higher than midpoint
        else:
            return self.binary_search(nums, target, m + 1, e)