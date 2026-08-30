import math

class PointDistance:
    def __init__(self, key: float, value: list[int]):
        self.key = key
        self.value = value

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pd_list: list[PointDistance] = []  # holds list of Point Distance

        # Calculate PointDistance based upon list
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)  # X & Y coordinates
            pointDistance = PointDistance(distance, point)
            pd_list.append(pointDistance)

        # Do a quick_sort
        self.quick_sort(pd_list, 0, len(pd_list) - 1)

        # Create new slice based off k
        result = []
        for i in range(k):
            result.append(pd_list[i].value)

        # Sort Point Distance List
        return result

    def quick_sort(self, arr, s, e):
        # Base Case
        if e - s + 1 <= 1:
            return

        # Algo
        pivot = arr[e].key
        left = s

        # Shift all values lower than pivot to the left pointer than increase
        for i in range(s, e):
            if arr[i].key < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        # Shift pivot with middle pointer
        arr[left], arr[e] = arr[e], arr[left]
        self.quick_sort(arr, s, left - 1)
        self.quick_sort(arr, left + 1, e)