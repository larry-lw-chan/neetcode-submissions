# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guess_number_helper(1, n)

    def guess_number_helper(self, s, e) -> int:
        # Base Case
        if s > e: return -1

        # Do Algo
        m = (s + e) // 2          # find middle ad use as guess
        guess_result = guess(m)   # Use API to see if fit

        print(guess_result)

        # Return number if correct
        if guess_result == 0:
            return m
        elif guess_result == -1:
            return self.guess_number_helper(s, m - 1)
        elif guess_result == 1:
            return self.guess_number_helper(m + 1, e)