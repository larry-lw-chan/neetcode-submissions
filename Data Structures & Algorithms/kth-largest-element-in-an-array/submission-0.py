import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        # Just chuck away max from head until k is reached
        for i in range(k):
            num = heapq.heappop(max_heap)
            if i == k - 1:
                return -num

        return 0