import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        return self.min_eating_speed_helper(piles, h, 1, piles[-1])

    def min_eating_speed_helper(self, piles: list[int], h: int, s: int, e: int) -> int:
        if s == e:
            return s  # calculated k

        # Algo
        k = (s + e) // 2
        eating_time = self.get_eatting_time(piles, k)

        if eating_time <= h:
            return self.min_eating_speed_helper(piles, h, s, k)
        else:
            return self.min_eating_speed_helper(piles, h, k + 1, e)

    def get_eatting_time(self, piles: list[int], k: int) -> int:
        eating_time = 0
        for banana in piles:
            eating_time += math.ceil(banana / k)
        return eating_time


if __name__ == "__main__":
    # piles = [312884470]
    # h = 312884469
    piles = [1, 4, 3, 2]
    h = 9
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    print(f"The min eating speed is {result}")
