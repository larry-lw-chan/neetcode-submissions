class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_consecutive = 0

        for num in nums:
            if num == 1:
                counter += 1
                if counter > max_consecutive:
                    max_consecutive = counter
            else:
                counter = 0
        
        return max_consecutive