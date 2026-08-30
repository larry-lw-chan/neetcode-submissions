class Solution:
    def __init__(self):
        self.memo = {}


    def climbStairs(self, n: int) -> int:
        # Return memo if available
        if n in self.memo: 
            return self.memo[n]
        
        # Base Case
        if n <= 1: 
            return 1         

        # Algo
        self.memo[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1) 
        return self.memo[n]