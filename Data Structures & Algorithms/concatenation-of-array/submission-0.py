class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        # Append 1
        for num in nums:
            ans.append(num)

        # Append 2
        for num in nums:
            ans.append(num)

        return ans