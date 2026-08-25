class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Need to first binary search based on rows
        row = self.row_searcher(matrix, target, 0, len(matrix) - 1)
        if row == -1:
            return False  # Return false if row not found

        # Once correct row found, now do binary search on columns
        column = self.column_searcher(matrix, target, row, 0, len(matrix[row]) - 1)

        if column == -1:
            return False
        else:
            return True

    def row_searcher(self, matrix: list[list[int]], target: int, s: int, e: int) -> int:
        # Base case - return false if search exhausted
        if s > e:
            return -1

        # Do algo
        m = (s + e) // 2  # Get middle,
        low = matrix[m][0]
        high = matrix[m][-1]

        # Check if target fits within range of 0 to last element
        if target >= low and target <= high:
            return m
        else:
            if target < low:
                return self.row_searcher(matrix, target, s, m - 1)
            else:
                return self.row_searcher(matrix, target, m + 1, e)

    def column_searcher(
        self, matrix: list[list[int]], target: int, row: int, s: int, e: int
    ) -> int:
        # Base case - return false if search exhausted
        if s > e:
            return -1

        # Do algo
        m = (s + e) // 2  # Get middle index
        value = matrix[row][m]  # Get middle value

        # If value matches target, return value
        if target == value:
            return m
        else:
            if target < value:
                return self.column_searcher(matrix, target, row, s, m - 1)
            else:
                return self.column_searcher(matrix, target, row, m + 1, e)

