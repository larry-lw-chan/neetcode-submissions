class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Loop pointer through array and swap value if higher than current idx
        for i in range(len(arr)):
            ptr = i + 1
            largest = 0

            while ptr < len(arr):
                # Pointer scans array and finds largest value
                if arr[ptr] > largest:
                    largest = arr[ptr] 

                # Increase Pointer
                ptr += 1

            # Assign largest value to arr[i]
            arr[i] = largest

        # Convert last array element to -1
        arr[len(arr) - 1] = -1

        return arr
