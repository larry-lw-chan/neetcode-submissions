import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Create max_head via - Heap inversion trick
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        # Find heavies two stones (x & y) by using max heap
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x == y:  # both stones destroyed
                continue
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, -y)

        if len(max_heap) == 1:
            return -max_heap[0]
        return 0