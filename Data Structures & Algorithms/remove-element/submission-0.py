class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer
        k = 0

        # first replace all 'val' found in nums with underscore
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # Return result
        return k
