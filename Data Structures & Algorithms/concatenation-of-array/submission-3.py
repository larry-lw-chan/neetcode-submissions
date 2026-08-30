class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        capacity = n * 2
        ans = [None] * capacity

        for i, num in enumerate(nums):
            ans[i], ans[i+n] = num, num

        return ans