# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        self.quicksort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def quicksort_helper(self, pairs: list[Pair], s: int, e: int):
        # Base Case
        if e - s + 1 <= 1:
            return pairs

        # Do Algo
        pivot = pairs[e].key
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot:  
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        # Move pivot to its correct sorted position
        pairs[e], pairs[left] = pairs[left], pairs[e]

        # Do Split
        self.quicksort_helper(pairs, s, left - 1)
        self.quicksort_helper(pairs, left + 1, e)





