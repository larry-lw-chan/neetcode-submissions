# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key: int = key
        self.value: str = value


class Solution:
    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        self.merge_sort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def merge_sort_helper(self, pairs: list[Pair], s: int, e: int):
        if e - s + 1 <= 1:
            return pairs

        # The middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.merge_sort_helper(pairs, s, m)

        # Sort the right half
        self.merge_sort_helper(pairs, m + 1, e)

        # Merge sorted halfs
        self.merge(pairs, s, m, e)

        return pairs

    # Merge in-place
    def merge(self, arr: list[Pair], s: int, m: int, e: int) -> None:
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        # Indexes
        i = 0  # index L
        j = 0  # index R
        k = s  # index 'arr'

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def debug(self, pairs: list[Pair], label: str):
        print(label)
        for node in pairs:
            print(node.key)
        print("########\n")