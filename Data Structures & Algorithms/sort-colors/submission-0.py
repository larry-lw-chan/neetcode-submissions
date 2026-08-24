class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]  # Index 0, 1, 2 represents red, white, and blue

        # Fill Bucket
        for num in nums:
            bucket[num] += 1

        # Iterate through bucket and modify nums in-place
        idx = 0

        # Calculate Red
        for i, v in enumerate(bucket):
            print(i)
            for _ in range(v):
                nums[idx] = i
                idx += 1